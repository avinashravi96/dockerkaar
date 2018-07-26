FROM python:3-onbuild
RUN python manage.py collectstatic
CMD ["python", "manage.py"]