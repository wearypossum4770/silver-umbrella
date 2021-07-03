import subprocess
from os import rename
from pathlib import Path

from celery import shared_task
from django.conf import settings
from PIL import Image

from users.models import Profile

size = (300, 300)


def convert_files_to_jpg(image_name):
    infile = image_name.name
    outfile = f"{image_name.stem}.jpg"
    if infile != outfile:
        try:
            with Image.open(infile) as img:
                img.thumbnail(size)
                img.save(f"{image_name.parent}/outfile")
        except OSError:
            print("cannot convert", infile)


def convert_images_to_jpg(image_name):
    subprocess.run(
        [
            "convert",
            f"./{'/'.join(image_path.parts)}",
            f"{str(image_path.parent)}/{image_path.stem}.jpg",
        ]
    )


def get_user_profiles():
    """
    Retrieves user's profile image.
    """
    profiles = Profile.objects.all()
    return [profile for profile in profiles]


def create_image_directory(__dirname):
    """
    Force creates new directory for each profile.
    """
    force_dir = f"{settings.MEDIA_ROOT}/{new_name}"
    Path(force_dir).mkdir(parents=True, exist_ok=True)
    return force_dir


def rename_profile_images(user_profile):
    """
    Renames, and relocates users' profile image to newly created user profile image directory.
    """
    initial_path = user_profile.image.path
    image_name = Path(initial_path)
    convert_files_to_jpg(image_name)
    convert_images_to_jpg(image_name)
    new_name = f"profile_pictures/{user_profile.user.username}/profile_image.jpg"
    profile.image.name = new_name
    new_path = create_image_directory(new_name)
    rename(initial_path, new_path)
    user_profile.save()


def convert_profile_images(infile):
    outfile = f"{infile.stem}.webp"
    subprocess.run(["cwebp", "-q", "80", infile, "-o", outfile])
    return "OK"


user_profiles = get_user_profiles()


@shared_task
def task_organize_profile_images():
    for user_profile in user_profiles:
        rename_profile_images(user_profile)


@shared_task
def task_convert_image_to_webp():
    for image in images:
        convert_profile_images(Path(image))
