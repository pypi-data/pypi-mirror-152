from django.db import migrations, models
from rygg.api.models import Model, Dataset, Project
from pathlib import Path
import logging
import os
import shutil

logger = logging.getLogger(__name__)
# rygg.settings isn't obeyed. Make it obey
LOG_LEVEL = os.getenv("PL_RYGG_LOG_LEVEL", "WARNING")
logger.setLevel(LOG_LEVEL)

HOME = Path.home()


def path_join(*paths):
    return os.path.join(*paths).replace("\\", "/")


def records_with_tilde(model_cls, field_name):
    return model_cls.objects.filter(**{f"{field_name}__startswith": "~"}).all()


def fix_record(r, model_name, id_field_name, field_name):
    try:
        id = getattr(r, id_field_name)
        pre = getattr(r, field_name)
        post = f"{HOME}{pre[1:]}"
        logger.debug(f"Updating {model_name} {id}: {pre} -> {post}")
        setattr(r, field_name, post)
        r.save()
    except Exception as e:
        logger.error(e)


def fix_field(app, model_name, field_name):
    try:
        model_cls = app.get_model("api", model_name)
        logger.info(f"Migrating {model_name}.{field_name}")
        records = records_with_tilde(model_cls, field_name)
        id_field_name = model_name.lower() + "_id"
        for r in records:
            fix_record(r, model_name, id_field_name, field_name)
    except Exception as e:
        logger.error(e)


def fix_paths(app):
    to_fix = [
        ("Project", "default_directory"),
        ("Model", "location"),
        ("Dataset", "root_dir"),
        ("Dataset", "location"),
    ]
    for cls, field in to_fix:
        fix_field(app, cls, field)


BAD = path_join(os.getcwd(), "~")
MODELS_SUBDIR = path_join("Documents", "Perceptilabs", "Default")
TO_MOVE_PARENT = path_join(BAD, MODELS_SUBDIR)
DEST_ROOT = path_join(HOME, MODELS_SUBDIR)


def move_one_model_dir(model_name):
    src_parent = path_join(TO_MOVE_PARENT, model_name)
    dest_parent = path_join(DEST_ROOT, model_name)
    logger.info(f"Putting {src_parent} back in place at {dest_parent}")

    def move_part(filename):
        src = path_join(src_parent, filename)
        dest = path_join(dest_parent, filename)

        # Is there a src to move?
        if not os.path.exists(src):
            logger.error(f"No {filename} to clean up at {src}.")
            return

        # Is there something in the way?
        elif os.path.exists(dest):
            logger.error(f"Skipping moving {src} to {dest} due to conflicts.")
            return

        logger.debug(f"Moving {src} to {dest}.")
        shutil.move(src, dest)

    if os.path.exists(dest_parent) and not os.path.isdir(dest_parent):
        logger.error(
            f"Skipping moving {model_name} from {src_parent} to {dest_parent} since the destination is not a directory."
        )
        return

    os.makedirs(dest_parent, exist_ok=True)
    move_part("checkpoint")
    move_part("model.json")

    if not os.listdir(src_parent):
        logger.info("Removing {src_parent}")
        shutil.rmtree(src_parent)


def move_model_dirs():
    if not os.path.isdir(BAD):
        return

    if not os.path.isdir(TO_MOVE_PARENT):
        return

    to_move = os.listdir(TO_MOVE_PARENT)
    for dir in to_move:
        move_one_model_dir(dir)


def fix(app, *args):
    fix_paths(app)
    move_model_dirs()


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0009_auto_20211121_1229"),
    ]

    operations = [
        migrations.RunPython(
            fix,
            # Unapply isn't needed since apply just expands the ~
            migrations.RunPython.noop,
        ),
    ]
