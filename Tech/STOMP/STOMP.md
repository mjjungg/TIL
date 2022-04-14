# STOMP

## STOMP란?

메세징 전송을 효율적으로 하기 위해 탄생한 프로토콜

- pub / sub 구조로 구성되어 메시지의 전송, 수신을 구분할 수 있어 개발자의 입장에서 명확하게 인지 후 개발할 수 있다.
- WebSocket 위에서 동작하는 프로토콜로, 클라이언트와 서버가 전송할 메시지 유형, 형식, 내용을 정의하는 매커니즘이다.

## STOMP의 동작

- 채팅방 생성 : Topic 생성 (우체통과 같은 역할)
- 채팅방 참여 : Topic 구독 (SUBSCRIBE)
- 채팅방 내부에서 메시지 송수신 : 해당 Topic으로 메시지 송신(pub), 수신(sub)
- Broker를 통해 타 사용자들에게 메시지 보내거나 서버가 특정 작업 수행하도록 메시지 보냄

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b42eb8c8-aa40-493e-9853-fd2cae29a257/Untitled.png)

### Spring에서의 STOMP

스프링에서 지원하는 STOMP → Spring WebSocket 애플리케이션은 STOMP Broker로 동작하게 됨

- Simple In Memory Broker를 이용해 해당 Topic에 SUBSCRIBE 중인 다른 클라이언트들에게 메시지 보내줌
- Simple In Memory Broker는 클라이언트의 SUBSCRIBE 정보를 메모리에 자체적으로 저장함

메시지를 외부 Broker에게 전달 → Broker는 WebSocket으로 연결된 클라이언트에게 메시지를 전달
