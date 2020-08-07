# Local
docker build ./web -t personal_page:v1.0.0
docker save personal_page:v1.0.0 > personal_page.tar
scp personal_page.tar root@68.183.101.65:/home/personal

# Server
ssh root@68.183.101.65
cd /home/personal
docker rm -f personal_page
docker rmi personal_page:v1.0.0
docker load < personal_page.tar
docker run -d -p 80:8000 --name personal_page personal_page:v1.0.0