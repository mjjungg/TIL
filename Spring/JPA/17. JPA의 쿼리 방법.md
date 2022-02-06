## JPA의 쿼리 지원

JPA는 다양한 쿼리 방법을 지원한다.

- **JPQL**
- JPQ Criteria
- **QueryDSL**
- 네이티브 SQL
- JDBC API 직접 사용

> JPQL과 QueryDSL 제일 많이 사용함!

## ⭐ JPQL

JPQL은 객체지향 쿼리 언어로 가장 단순한 조회 방법을 제공한다. 

*예) age가 20살 이상인 회원 모두 검색하는 경우* 

JPQ를 사용하여 엔티티 객체를 중심으로 개발할 때 검색을 하는 경우에도 테이블이 아닌 엔티티 객체를 대상으로 검색한다. 하지만 모든 DB 테이블을 객체로 변환하여 검색할 순 없다. 

→ 어플리케이션이 필요한 부분만 DB에서 가져어려면, 검색 조건의 SQL 필요하다!

- JPA에서 SQL을 추상화하여 JPQL을 제공한다. → 특정 DB SQL에 의존하지 않는다.
- JPQL은 엔티티 객체를 대상으로 쿼리를 날린다. (SQL은 DB 테이블 대상으로 쿼리 날림)
- SQL과 같이 SELECT, FROM, WHERE, GROUP BY, HAVING, JOIN 절을 지원한다.

### 😋 SELECT문 맛보기

```jsx
String jpql = "select m from Member m where m.age >= 20";
List<Member> result = em.createQuery(jpql, Member.class)
											.getResultList();
```

여기서 m은 엔티티 자체를 가리킨다. 

## Criteria

JPQL로는 동적 쿼리 생성하기가 힘들다. 

예를 들어 userName이 null이 아닌 경우에만 where userName like ~를 해야하는 경우를 생각해보자. 이 경우에는 JPQL은 결국 String이기 때문에 쿼리를 조각조각 붙여야 한다. 이 과정에서 띄어쓰기 신경써야 하고, ... 요론 과정에서 에러 많이 발생한다. 

→ 이를 해결하기 위해 Criteria사용한다!

**BUT**, criteria는 SQL처럼 무엇을 하는지 직관적으로 코드에 보이지 않아서 유지보수 하기 힘들다.

## ⭐ QueryDSL

QueryDSL은 오픈소스 라이브러리로 문자가 아닌 자바 코드로 JPQL을 작성할 수 있다. 

- JPQL 빌더 역할 → ??
- 동적쿼리 작성 편리함

## 네이티브 SQL

특정 DB의 SQL을 직접 사용하는 기능이다. 

- 특정 DB에 의존적이다.

```jsx
List<Member> resultList =
em.createNativeQuery(sql, Member.class).getResultList();
```

## JDBC 직접 사용

JPA를 사용하면서 JDBC 커넥션을 직접 사용 또는, 스프링 JdbcTemplate, 마이바티스를 같이 사용한다. 

⚡ 영속성 컨텍스트를 쿼리 날리기 전에 강제로 플러시 해줘야 함  

→ WHY?

persist가 아니라 commit했을 때 데이터가 db에 들어감 → commit전에 쿼리 날리면 flush가 호출됨
jpa에서 flush는 commit, 쿼리 날릴때 동작 함
하지만, jpa가 아닌 스프링 db connection 같은 경우 flusth가 자동으로 실행 안 되기 때문에 강제로 flush해야 함
