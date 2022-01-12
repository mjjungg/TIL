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
selet m from Member m where m.username=:파라미터명
query.setParameter("파라미터명", "xxx");
```

- 위치 기준 → 잘 사용 안함

## SELECT 절

### 프로젝션

SELECT 절에 조회할 대상을 지정하는 것을 프로젝션이라 한다.

- 엔티티 프로젝션 : select m from Member m

→ 여기서 m은 영속성 관리 대상임

```jsx
List<Member> result = em.createQuery(" 
selct m from Member m", Member.class) 
.getResultList(); 
Member findMember = result.get(0); 
findMember.setAge(20);
```

findMember는 영속성 관리 대상이기 때문에 setAge() 했을 때 findMember의 age 값이 바뀐다.

- 엔티티 프로젝션 : select m.team from Member m
- 임베디드 타입 프로젝션 : select m.address from Member m
- 스칼라 타입 프로젝션 : select m.id, m.age from Member m
- DISTICT로 중복 제거

### 프로젝션으로 여러 값 조회

1. Query 타입으로 조회
2. Object[] 타입으로 조회
3. new 명령어로 조회 → 제일 깔끔함! 

    3-1. MemberDTO라는 클래스를 만들고, 가지고 오려는 여러 값을 속성으로 넣음

    3-2. select절에서 마치 생성자를 호출하듯이 new 키워드로 조회함 

    💡 new 다음 클래스명을 명시할 때 패키지 명을 포함하여 전체 클래스 명을 명시해야 함

    ```jsx
    // MemberDTO 클래스 생성
    public class MemberDTO{
    	private userName;
    	private age;

    	// 생성자, getter, setter
    } 

    // jpa 메인 실행 
    List<MemberDTO> result = em.createQuery(" select new jpql.MemberDTO(m.username, m.age)
    	from Member m", MemberDTO.class).getResultList();
    ```

    ## 페이징 API

    순서 자를 때 (MySQL에서 limit절)

    - setFirstResult(int startPosition) : 조회 시작 위치
    - setMaxResults(int maxResult) : 조회할 데이터의 수

    ```jsx
    String jpal = "select m from Member m order by m.age";
    List<Member> resultList = em.createQuery(jpql, Member.class)
    .setFirstResult(3).setMaxResult(10).getResultList();
    ```

    ## 조인

    ### ON절을 이용한 조인

    1. 조인 대상 필터링 

        팀 이름이 teamA인 팀만 조인

        **SQL** 

        from Member m join m.team t on 

        m.teamId=t.id and t.name="teamA"

        **JPQL**

        from Member m join m.team t on t.name="teamA"

    1. 연관관계 없는 엔티티 외부 조인

        from Member m  join Team t on m.username = t.name

## JPA에서의 서브 쿼리

- where, having절에서만 사용 가능
- select 절은 하이버네이트에서 지원하여 가능
- from절 서브 쿼리 불가능 → 조인으로 풀어서 해결

## 사용자 정의 함수

사용하는 DB 방언을 상속받아 사용자 정의 함수를 등록함
