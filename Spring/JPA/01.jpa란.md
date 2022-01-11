# JPA란?

Java Persistence API로, 자바에 있는 데이터를 영구적으로 기록할 수  있는 환경을 제공하는 API이다.

자바 진영의 ORM 기술의 표준이다.

### ORM?

Object-relational mapping의 약자로, 객체는 객체대로 설계하고 관계형 DB는 관계형 DB대로 설계한다는 의미이다. ORM 프레임워크가 중간에서 매핑해준다. 

spring boot는 자바를 사용한다. → 객체 지향적 설계!

but, DB는 SQL으로 동작

🔥 객체 VS 관계형 데이터베이스 

패러다임의 불일치 발생 → JPA를 통해 객체 중심의 설계로 패러다임의 전환 가능함!

## SQL 중심적인 개발의 문제점?

객체 → SQL 변환 → DB저장

1. 많은 쿼리 날려야 함... 🤮

    CRUD(INSERT INTO... , UPDATE... )

2. 만일 필드라도 추가한다면? 

    INSERT INTO ...

    조인하는 테이블까지 다 수작업으로 INSERT문 날려야 함...

⇒ SQL에 의존적인 개발하게됨 → 이 시간을 좀 더 아껴서 기능, 성능 개발에 몰두하자!!

# JPA 동작 방식

애플리케이션과 JDBC 사이에서 JPA가 동작한다.

JPA가 Entity분석해서 SQL생성하고, JDBC API를 통해 DB로 쿼리를 날린다. 

# CRUD → JPA

- `jpa.persist(member)` : 저장
- `jpa.find(memberId)` : 찾기
- `member.setName("name1")` : 수정
- `jpa.remove(member)` : 삭제

→ 필드를 추가해도 JPA가 알아서 조인하는 테이블까지 처리해줌 

# JPA의 성능 최적화 기능

1. 1차 캐시 

    JPA는 find로 조회하면 1차 캐시라는 곳에 가져온 정보를 저장해둔다. 이후 또 같은 정보를 조회하면 빠르게 1차 캐시에서 정보를 가져올 수 있다. 

2. 쓰기 지연 

    트랜잭션을 커밋할 때까지 쿼리를 모았다가 커밋하는 순간 한방에 SQL전송한다.

3. 지연로딩 vs 즉시로딩

    객체가 사용될 때마다 즉시 로딩 vs 한 번에 join한 객체까지 모두 가져옴 

    → 코드는 지연로딩으로 짜놓고 최적화 필요할 때 옵션으로 즉시 로딩하게 끔!!
