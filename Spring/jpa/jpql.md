## JPQL

JPQL은 테이블을 대상으로 쿼리하는 것이 아니라 엔티티 객체를 대상으로 쿼리한다.

## 문법

- 엔티티와 속성은 대소문자 구분한다.(Member, address)
- JPQL 쿼리 키워드는 SQL과 마찬가지로 대소문자 구분X(select, where..)
- from 절에서 **alias는 필수!!!!**

## 반환 타입

- TypedQuery : 반환  타입 명확한 경우 → 두 번째 파라미터에 타입 명시
- Query : 반환 타입이 불명확한 경우

```jsx
TypedQuery<Member> jpql = em.createQuery("
				select m from Member m", Member.class);

Query query = em.createQuery("
				select m.id, m.name from Member m");
```

## 결과 조회 API

- query.getResultList() : 결과가 하나 이상일 때 → 리스트 반환 결과가 null이면 빈 리스트 반환
- query.getSingleResult() : 결과가 정확히 언제나 한개 일 때!!

→ 결과가 없으면 javax.persistence.NoResultException

→ 둘 이상이면 

javax.persistence.NonUniqueResultException

💡 이 두 가지 에러는 많이 발생하는 에러이므로 기억해두기! 

## 파라미터 바인딩

- 이름 기준

```jsx
selet m from Member m where m.username=**:username**
query.setParameter("**username**", "xxx");
```

- 위치 기준 → 잘 사용 안함

## SELECT 절

### 프로젝션

SELECT 절에 조회할 대상을 지정하는 것을 프로젝션이라 한다.

- 엔티티 프로젝션 : select m from Member m

→ 여기서 m은 영속성 관리 대상임

- 엔티티 프로젝션 : select m.team from Member m
