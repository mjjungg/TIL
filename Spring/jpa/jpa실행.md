## 프로젝트 생성

1. 생성 

`artifactId` : 저장되는 폴더명

`groupId` : 프로젝트를 식별해주는 고유 아이디(프로젝트에서 컨트롤하는 도메인 이름과 동일하게 입력)

2. porm.xml에 라이브러리 추가

- JPA 하이버네이트
- H2

3. src/main/resources에 `META-INF/persistence.xml` 생성 

위치가 표준으로 정해져 있기 때문에 무조건 따라야 함!

JPA 설정파일이다.

- JPA는 특정 DB에 종속적이지 않아서 언제든지 MySQL, Oracle 등의 DB로 갈아끼울 수 있다.

## JPA 구동 방식

1. Persistence가 META-INF/persistence.xml에서 설정 정보를 조회한다.
2. Persistence가 EntityManagerFactory를 통해 EntityManager를 생성한다.

 

EntityManagerFactory는 오직 한 개 생성해서 애플리케이션 전체에서 공유!

EntityManager는 자바에서의 컬랙션과 같은 존재이다!

## 객체 생성과 테이블 매핑

자바 파일에서 클래스명 위에 `@Entity`

를 넣으면 jpa를 사용하는 얘라고 인식함!

프로퍼티 위에 `@ID` 를 넣으면 DB PK와 매핑됨

## JPQL

전체 회원 검색하고 싶을 때, ID가 5이상인 회원만 검색하고 싶을 때 등, 엔티티에서 많은 양의 검색하고 싶을 때 사용 

- 테이블이 아닌 객체를 대상으로 검색하는 **객체 지향 쿼리**이다.
