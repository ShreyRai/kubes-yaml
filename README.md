For Probes folder:
I have used K3D for kubernetes hands-on. So if we create the image in the node then the image will not automatically go to k3d cluster as the kubernetes is running
on the docker. So in order to copy the image use this command:

`$k3d image import probe-app:v1 -c mycluster`

