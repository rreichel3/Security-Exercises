FROM golang
MAINTAINER Robert Reichel
ADD ./TimingAttackServer /go/src/github.ncsu.com/rjreiche/TimingAttackServer
RUN go install github.ncsu.com/rjreiche/TimingAttackServer
ENTRYPOINT /go/bin/TimingAttackServer
EXPOSE 8002
EXPOSE 8080