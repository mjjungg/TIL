## 경로 표현식이란?

.으로 접근하여 객체 그래프를 탐색하는 것

- 상태 필드 : m.id

    경로 탐색의 끝이므로 더이상 탐색 X

- 연관 필드

    - 단일 값 연관 필드 : m.team   → 엔티티

    - 컬렉션 값 연관 필드 : m.orders → 컬렉션 

### 단일 값 연관 필드

묵시적으로 내부 조인이 발생하고 탐색이 가능하다. 

`JPQL`

```sql
select m.team from Member m
```

으로 JPQL 날리면

`SQL`

```sql
select t.* from Member m inner join Team t on m.team_id=t.id
```

다음과 같은 sql처럼 동작한다.  

### 컬렉션 값 연관 필드

묵시적으로 내부 조인이 발생하지만 탐색이 불가능하다.

예)

```sql
select t.members.id from Team t
```

는 안 됨!!

> 💡 가급적 묵시적 조인 대신 명시적 조인을 사용해라!
