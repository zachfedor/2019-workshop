# Docker Labs: Beginner


## Running Your First Container

Get an image from the docker registry and save it locally: `docker pull alpine` (Alpine is super light Linux distro)

List pulled images with `docker images`

Run a container by picking an image and command to run: `docker run alpine ls -l`

The `run` command will exit after the container is done running its command. Keep it open with `run -it` for an interactive session, like using `bash` or a similar command.

List running containers with `docker ps`. Add the `-a` option to see all that have been run recently.


## Web Apps with Docker

`docker run -d dockersamples/static-site`

This image contains a static website. Running with the `-d` option detaches the container so it can run in the background and you regain control of the prompt.

To stop a running container, run `docker ps` to get its container ID then run `docker stop <id>`

`docker run --name static-site -e AUTHOR="Your Name" -d -P dockersamples/static-site`

This command adds a few new flags:
- `-P`: publishes exposed ports (view ports with `docker port <container_name>`)
- `-p`: routes port to host from container, like `8888:80`
- `-e`: pass environment variable to container in `KEY="value"` pairs
- `--name`: give a custom name to the container

Use `docker rm -f <container_name>` as a shortcut to stop and remove a container.


## Creating Docker Images

Run `docker images` to see a list of images you've already pulled from the registry.

Images are like git repos, committed versions have unique IDs and can be tagged with a version number or `latest`, for example. Child images are built off of base images, usually an OS. Official images are sanctioned by a dedicated team (i.e. `python`, `alpine`, etc), user images are prefixed by the username.

Dockerfiles are used to create images: from what base, location of project code, dependencies, start-up commands, etc. Some Dockerfile keywords:

- `FROM`: extend from base image, like `alpine:latest`
- `RUN`: run commands to create the image
- `COPY`: move files into the image
- `EXPOSE`: open a port
- `CMD`: the default command to run when the container starts

Run `docker build .` in the directory with the Dockerfile to create the image, passing the optional `-t` flag to tag it with your Docker Hub username and image name. Verify with `docker images` and see if it's listed.

After the image is built, you can run it with `docker run username/imagename` opening any needed ports or naming it with the `-p` and `--name` options.

If it works, you can host it on the registry with `docker push username/imagename`.


## Deploying To A Swarm

