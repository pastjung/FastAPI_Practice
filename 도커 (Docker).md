06292021

# 도커 (Docker)



## 1. 도커란?

   * 도커는 컨테이너 기반 가상화 도구
   * 도커는 리눅스 상에서 컨테이너 방식으로 프로세스를 격리해서 실행, 관리할 수 있도록 도와주는 프로그램
   * 일종의 가상환경을 (vmware 등) 만들어 어떤 컴퓨터 환경에서도 동일한 애플리케이션을 실행시킬 수 있게끔 하는 도구

---

   * 도커는 아래와 같은 프로세스로 실행된다:
     1. 도커에서 베이스가 될 OS 이미지 (image)를 빌드 하고
     2. 빌드된 이미지들 실행시키면 이것이 컨테이너 (container)가 된다.
     3. 컨테이너가 실행되면 해당 컨테이너 내의 애플리케이션이 동작된다.

   

   * 상기 프로세스는 CD 를 생각하면 쉽다:

     1. 공 CD 에 윈도우, 리눅스 같은 운영체제와 필요한 프로그램을 설치하고 CD를 굽는다 (= 도커 이미지 빌드)

     2. 만들어진 CD를 CD-ROM 드라이브에 넣어서 실행시킨다.

        (= 도커 컨테이너 실행)

     3. CD-ROM 이 CD 를 읽으면서 우리는 CD 안의 운영체제를 사용하여 우리가 같이 설치한 프로그램을 실행시킬 수 있다. (= 도커 컨테이너 내 프로그램 실행)

---





## 2. 도커의 장점
1. 환경에 구애받지 않고 개발한 프로그램을 실행/배포할 수 있다.

   * 가령 Java로 만든 프로그램을 실행시키기 위해선 컴퓨터에 Java JVM, JRE 등 이 필요하다.

   * 그 외 필요한 라이브러리, 의존성 패키지 설치가 필요할 수 있따.

   * 개발을 한 환경에서는 작동을 하지만, 다른 컴퓨터 환경에서는 버전문제등으로 실행이 제대로 되지 않을 수 있다.

   * 도커는 이미지 내에 애플리케이션 구동에 필요한 파일까지 모두 설치해버려서 어떤 환경에서던 실행이 가능하다.

   

2. 한번 빌드한 이미지는 불변한다.

   * 한번 CD를 구으면 CD 안의 내용을 삭제할 수 없는것처럼, 도커또한 한번 이미지를 빌드하면 아무리 수정을 해도 다음에 다시 실행시킬때 기존 상태가 보존된다.

   * 극단적으로 ```sudo rm -rf / --no-preserve-root``` 을 날려도 다음번에 컨테이너를 실행시키면 기존 상태로 복구되어 있다.

   * 즉 서버관리에 매우 유용하다.

     

3. 관리와 공유가 쉽다.
   * 만들어진 이미지는 수정과 재사용이 가능하다.
   * 깃과 같은 저장소를 사용한 빠른 공유가 가능하다.
   * 여러개의 컨테이너를 실행시켜서 서로 상호작용 하게끔 클러스터링이 가능하다.





## 3. 도커 맛뵈기

  ### 1) 도커 설치하기

> 하기 버전의 리눅스 기준으로 설치
>
> - Ubuntu Hirsute 21.04
> - Ubuntu Groovy 20.10
> - Ubuntu Focal 20.04 (LTS)
> - Ubuntu Bionic 18.04 (LTS)
> - Ubuntu Xenial 16.04 (LTS)

* 도커는 하기 공식 홈페이지 의 커맨드를 따라 설치할 수 있다. 

  https://docs.docker.com/engine/install/ubuntu/

```bash
# 기존에 도커가 설치되어 있다면 삭제한다.
$ sudo apt-get remove docker docker-engine docker.io containerd runc
```

```bash
# apt 패키지를 업데이트 하며 도커 저장소를 설치한다.
$ sudo apt-get update

$ sudo apt-get install \
apt-transport-https \
ca-certificates \
curl \
gnupg \
lsb-release
```

```bash
# 도커 공식 GPG 키를 삽입한다.
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

```bash
# 도커 저장소를 지정한다.
$ echo \
"deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

```bash
# 도커를 설치한다.
$ sudo apt-get update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io
```

```bash
# 도커가 설치되었는지 확인한다.
$ sudo docker run hello-world
```





### 2) 도커 실행해보기

* 도커를 사용하여 센트OS 구동시키기

``` bash
# 차이를 보기 위해 현재 리눅스의 버전을 확인해보자:
$ cat /etc/lsb-release
```

```bash
# 결과
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=20.04
DISTRIB_CODENAME=focal
DISTRIB_DESCRIPTION="Ubuntu 20.04.2 LTS"
```

> 현재 (본인) 컴퓨터 기준 우분투 20.04 버전이 설치되어 있는것을 확인할 수 있다.



* 이미지 구동

```bash
$ (sudo) docker run -it --rm centos:latest bash
```

* ```bash``` 는 쉘을 사용하기 위해 bash 명령어를 실행시킨다는 의미이다.

```bash
# 결과
Unable to find image 'centos:latest' locally
latest: Pulling from library/centos
7a0437f04f83: Pull complete
Digest: sha256:5528e8b1b1719d34604c87e11dcd1c0a20bedf46e83b5632cdeac91b8c04efc1
Status: Downloaded newer image for centos:latest
[root@ab4061aff0f9 /]#
```

```bash
# 다시 차이를 보기 위해 아래 커맨드로 버전확인을 해보자
[root@ab4061aff0f9 /]# cat /etc/redhat-release
CentOS Linux release 8.3.2011
```

> 변한것이 없어 보이지만 현재 우리는 CentOS 운영체제를 사용중임을 확인할 수 있다.



* 도커 종료하기

```bash
[root@ab4061aff0f9 /]# exit
```

  

  

  ### 3)  docker run 옵션들

  ```bash
  # 기본 포맷
  $ (sudo) docker run [OPTIONS] IMAGE[:TAG|@DIGEST] [COMMAND] [ARG...]
  ```

  #### 			[OPTIONS]

   * ```-i``` 은 stdin 인터페이스를 열어준다.
   * ```-t``` 는 도커 컨테이너를 터미널로 접속해 쉘 명령어를 입력할 수 있게 한다.
   * ```--rm``` 은 컨테이너를 일회성으로 실행할때 쓰인다. 컨테이너가 종료될 때 컨테이너를 죽인다 (kill)
   * 

  * ```-d``` : 도커를 데몬으로 실행시킨다 (백그라운드로 실행시킨다)

  * ```-p```: 실행시키려는 컨테이너의 포트를 연다. 

    ​		예) ``` -p 80:8080``` 의 의미는 외부에서 80번 포트로 접속하면 도커 내부의 8080포트로 리다이렉팅 시킨다는 의미이다.

  * ```-e``` : 컨테이너 내의 환경변수를 설정한다.

    ​		예) ```-e ROOT_PATH=/src/workspace/``` 의 의미는 컨테이너 내의 ```ROOT_PATH``` 변수에 ```/src/workspace/``` 를 설정하겠다는 의미

  * ```-w``` : ```WORKDIR``` 을 설정한다. ```-w /etc ``` 는 컨테이너 내 기본 ```pwd``` 를 ```/etc``` 로 설정하겠다는 의미이다.

  * ``--entrypoint`` : 컨테이너가 실행될 때 , 뒤의 인자가 실행 명령어로써 실행된다

    ​		예) 

  ```bash
  $ (sudo) docker run -it --rm --entrypoint ls centos:latest
  bin  etc   lib    lost+found  mnt  proc  run   srv  tmp  var
  dev  home  lib64  media       opt  root  sbin  sys  usr
  ```

  * 외에 많은 옵션들이 있으니 찾아서 연습해볼것.

  



## 4. 도커 가지고 놀아보기

* 앞서 보았던것 처럼 도커는 격리된 환경을 구성시켜 원하는 프로그램을 구동시킬 수 있읍니다

* 하지만 컨테이너가 종료되면 컨테이너 내의 변경사항 (파일 생성, 수정, 제거 등등) 이 모두 초기화 되는 문제가 있다.

* 즉 도커 컨테이너 내에서 아무리 아파치 서버를 설치한다 해도, 도커를 종료하는 순간 이 아파치 서버 애플리케이션은 삭제가 되요.

* 이를 어떻게 극복하여 우리가 원하는 프로그램을 실행/배포 시킬 수 있을까?

* 답은 ```Dockerfile``` 작성입니다.

  

  


  ### 1) Dockerfile 이란?


  * 상기 ```docker run ``` 커맨드는 이미 만들어진 도커 이미지를 컨테이너로 만들어서 실행시키는것에 불과합니다.
  * 아파치 서버나 다른 우리가 필요한 애플리케이션들이 포함된 도커 이미지가 이미 있다면 문제는 없지만, 대부분의 경우는 그러지 않아요.
  * ```Dockerfile``` 은 우리가 필요한 프로그램들을 작성한 명세서의 개념이라 생각하면 됩니다.
  * ```Dockerfile``` 안에 우리가 필요한 프로그램 또한 명세 한 뒤 이를 실행시킴으로 우리가 원하는 이미지를 만들 수 있습니다.
  * 이를 이미지를 빌드 (build) 한다 합니다.

  

  

  ### 2) Dockerfile 작성하기

  * 도커파일은 확장자 (extention) 없이 ```Dockerfile``` 만드는것에서 시작합니다.
  * 텍스트에디터나 ```vi```, 혹은 사용하고 있는 편집툴로 하기와 같이 작성해봅시다.

```dockerfile
FROM python:3.8.6-buster
RUN mkdir -p /app
RUN ls
WORKDIR /app
```

```bash
# Dockerfile을 작성한 경로에서 아래 커맨드를 실행시키자
$ (sudo) docker build -t python-test:sample_latest .
```

```bash
# 결과
Sending build context to Docker daemon  3.072kB
Step 1/4 : FROM python:3.8.6-buster
 ---> d1bfb3dd9268
Step 2/4 : RUN mkdir -p /app
 ---> Running in 15bd911ba96b
Removing intermediate container 15bd911ba96b
 ---> 16be0600e8fb
Step 3/4 : RUN ls
 ---> Running in 610d8d4bc81d
app
bin
boot
dev
etc
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
Removing intermediate container 610d8d4bc81d
 ---> 3fde0c52f248
Step 4/4 : WORKDIR /app
 ---> Running in 1da69897b8d4
Removing intermediate container 1da69897b8d4
 ---> 958ecae05e35
Successfully built 958ecae05e35
Successfully tagged python-test:sample_latest
```

> * 도커가 이미지를 빌드 중 ```RUN ls``` 를 실행해서 컨테이너 내부의 파일들을 출력한것을 확인할 수 있습니다.
>
> * ```docker build -t python-test:sample_latest .``` 에서 ``` -t ``` 옵션으로 이미지의 이름과 버전등의 태그를 붙일 수 있다.
>
> * ' . ' 으로 현재 위치에 ```Dockerfile``` 이 있다는걸 명시해준다.





  ### 3) 빌드한 도커 이미지 확인 후 실행하기

```bash
# 현재 로컬 저장소에 존재하는 도커 이미지들을 보여준다.
$ (sudo) docker image ls
```

```bash
# 결과
REPOSITORY                      TAG             IMAGE ID       CREATED          SIZE
python-test                     sample_latest   170de0dc6d83   49 seconds ago   882MB
```

> 도커 이미지를 빌드 한다는것은 공 CD에 프로그램을 넣고 굽는다고 생각하면 쉽습니다.
>
> 도커 이미지가 잘 빌드 된것을 확인할 수 있다. ```IMAGE ID``` 를 사용하여 컨테이너를 실행시킬 수 있다.

```BASH
# 빌드한 이미지 컨테이너 실행하기
$ (sudo) docker run -it 170de0dc6d83 bash
```

```bash
# 결과
root@a2ad823c2775:/app# 
```

> ```IMAGE ID``` 는 이미지를 빌드할때마다 다르니 자신의 ```IMAGE ID```를 실행시키자.
>
> build 할때 명세한 ```WORKDIR /app``` 에 의해 ```/app``` 경로가 기본 경로인것을 확인할 수 있다.





  ### 4) 컨테이너 종료, 컨테이너 삭제,  및 이미지 삭제하기

#### i. 컨테이너 종료하기 (kill)

   *	새로운 CMD 창에서 현재 가동중인 컨테이너 및 ```CONTAINER ID``` 를 확인합시다

```bash
# 현재 실행중인 도커 컨테이너 목록을 보여줍니다
$ (sudo) docker ps 
```

```bash
# 결과
CONTAINER ID   IMAGE          COMMAND      CREATED          STATUS          PORTS             NAMES
269cb4793a7a   centos:latest  "bash"       11 seconds ago   Up 10 seconds                     blissful_golick
```

```bash
# 도커 컨테이너 죽이기 (kill)
$ (sudo) docker kill 269cb4793a7a
```

```bash
# 결과
269cb4793a7a
```

> 상기와 같이 죽이고자 하는 ```CONTAINER ID``` 가 표시되어야 컨테이너가 정상적으로 종료된것입니다
>
> 컨테이너를 종료한다 라는 의미는 컴퓨터에서 CD안의 프로그램을 종료했다는 의미로 생각하면 쉽습니다.



#### ii. 컨테이너 삭제하기

```bash
# 사용했던 모든 컨테이너 목록 보기
$ (sudo) docker container ls -la
```

```bash
# 결과
CONTAINER ID   IMAGE   			COMMAND            CREATED        STATUS                    PORTS             NAMES
a2ad823c2775   170de0dc6d83 	"bash"             42 hours ago   Exited (0) 1 hours ago               	  	  blissful_golick
```

```bash
# 컨테이너 삭제
$ (sudo) docker rm a2ad823c2775
```

```bash
#결과
a2ad823c2775
```

> 컨테이너를 삭제한다는 의미는 CD-ROM 에서 CD를 꺼낸다는 의미로 생각하면 쉽습니다.



#### iii. 이미지 제거하기

```bash
# 보유하고 있는 이미지 확인하기
$ (sudo) docker image ls
```

```bash
# 결과
REPOSITORY                      TAG             IMAGE ID       CREATED        SIZE
python-test                     sample_latest   170de0dc6d83   3 hours ago    882MB
```

```bash
# 도커 이미지 제거하기
$ (sudo) docker rmi 170de0dc6d83
```

```bash
# 결과
Untagged: python-test:sample_latest
Deleted: sha256:170de0dc6d8306b1ae94d77c9f4e7eb32a434e74749bc2399735a320802c3bd0
```

> 이미지를 삭제한다는 의미는 CD를 깨 부순다는 의미로 생각하면 쉽습니다.





## 5. 도커로 아파치 서버 올려보기

### 1) Dockerfile 명세하기

```bash
FROM ubuntu:20.04
ADD . /app     
# 파일을 이미지에 추가한다. 파일은 Dockerfile이 위치한 디렉터리에서 가져온다.

WORKDIR /app
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt install apache2 -y
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2/apache2.pid 

EXPOSE 80					# 80번 포트를 개방하겠다는 의미입니다.

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
```

> 도커에 사용하는 많은 커맨드들은 찾아보면서 알아보도록 합시다.





### 2) Dockerfile 빌드하여 도커 이미지 생성하기

```bash
# Dockerfile 이 있는 경로에서 스크립트를 날립니다.
$ (sudo) docker build -t test_apache:1.0.0 .
```



### 3) 도커 이미지 실행시키기

```bash
$ (sudo) docker run -d -p 80:80 test_apache:1.0.0
```



### 4) 브라우저에서 접속해보기

```bash
# 크롬이나 IE 같은 브라우저에서 접속을 해봅시다
localhost:80
```



### 5) 생성한  컨테이너 내부 접속해보기

```bash
# 먼저 CONTAINER ID 를 획득합니다
$ (sudo) docker container ls
```

​		혹은

```bash
$ (sudo) docker ps
```

```bash
# 결과
CONTAINER ID  IMAGE             COMMAND                 CREATED         STATUS         PORTS        					NAMES
be4e5d93deea  test_apache:1.0.0 "/usr/sbin/apache2ct…"  2 minutes ago   Up 2 minutes   0.0.0.0:80->80/tcp, :::80->80/tcp  pensive_lamport 
```

```bash
$ (sudo) docker exec -it be4e5d93deea bash
```

```bash
# 결과
root@be4e5d93deea:/app#
```





## 6. 마무리

* 이제 도커로 격리된 환경에서 애플리케이션을 실행하는 방법을 배웠습니다.

* 다만 우리가 사용할 프로그램들 또한 도커 내부로 옮겨져야 이들도 격리된 환경에서 사용이 됩니다.

* ```docker cp``` 같은 커맨드로 우리가 원하는 프로그램을 도커 컨테이너에 옮길수도 있습니다.

* 빌드를 할때 이 프로그램들을 같이 포함시킬수도 있지만 DB 서버 같이 데이터가 변동이 되는 프로그램은 컨테이너가 종료되면 DB의 데이터도 삭제되는 문제점이 있습니다.

* ```Dockerfile``` 명세할때 ```VOLUME``` 같은 커맨드로 로컬 환경의 드라이브를 마운트 시켜 컨테이너에서 발생하는 데이터를 로컬에 저장시키고, 컨테이너를 재시작 했을때 이를 불러올 수도 있습니다.

* 위 부분은 직접 찾아서 실습을 해 보시길 바랍니다.

* 하지만 도커는 만능이 아닙니다.

* 하나의 서버에는 하나의 프로그램이 구동되는것이 일반적인것 처럼, 하나의 컨테이너 내에서는 하나의 프로그램이 구동되는것이 일반적이고 이상적입니다.

  (ex. 웹서버, DB서버, 엔진서버 등등..)

* 그렇기때문에 실무에서는 이미지를 여러개 빌드하고, 각각의 ```Dockerfile```을 명세하고, 각개의 컨테이너를 실행시키며, 컨테이너 마다의 옵션값을 조정하여서 실행시키는 귀찮고 장황한 작업이 필수입니다.

* 그것을 해결하기 위해서 나온 솔루션이 바로 ```docker-compose``` 입니다.

* ```docker-compose``` 에 관해서는 다음시간에...





## APPENDIX

> ```Dockerfile``` 옵션 설명
>
> * ```FROM``` : 어떤 이미지를 가져와 os 의 베이스로 실행할지 결정한다 ( ex. python:3.8.6-buster, ubuntu:18.04 )
>
> * ```LABEL``` : 이미지에 메타데이터를 추가한다. (원하는 조건의 컨테이너, 이미지를 쉽게 찾기 용이하게 해준다)
>
> * ```ADD``` : 파일을 이미지에 추가한다. Dockerfile 이 위치한 폴더에서 특정 파일을 가져와 원하는 경로에 추가해준다. 
>
>   ​			(다만 해당 경로가 도커 이미지 내에 있어야 한다)
>
> * ```RUN``` : 이미지를 만들기 위해 컨테이너 내부에서 명령어를 실행하게끔 한다. 이미지를 만들때 사용되는 명령어! (CMD 와 차이가 있다)
>
> * ```WORKDIR``` : cd 명령어와 비슷하지만, 디렉토리를 workdir 로 전환하면 그 뒤의 모든 RUN, CMD, ENTRYPOINT 등등은 해당 경로에서 시작한다.
>
> * ```CMD``` : 컨테이너가 실행될때마다 실행할 명령어. container run시 다른 인자가 전달되면 CMD 는 무시된다. 
>
>   ​			( RUN 은 이미지를 만들때 실행되며, CMD 는 컨테이너가 만들어질때마다 실행된다 )
>
>   
>
> * ```ENTRYPOINT``` : 어떤 경우에든 컨테이너가 실행될때 이 값이 인자로써 실행됨 
>
>   ​						(다른 인자가 실행되어도 실행. CMD 는 Default Arguments 같은 느낌) docker run 시 추가인자가 전달되지 않는 이상, CMD 와 						 ENTRYPOINT 는 동시에 실행된다.
>
> * ```EXPOSE``` : 노출시킬 포트번호를 지정한다 ( ex. 80, 8080, 21 )
>
> 그 이외 많은 키워드들이 있습니다. 특히 ```VOLUME``` 은 중요하니 잘 찾아봅시다.