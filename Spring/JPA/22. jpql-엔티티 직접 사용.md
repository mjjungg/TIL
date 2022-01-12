## 엔티티 직접 사용 → 기본 키 값 사용

JPQL에서 엔티티를 직접 사용하면, SQL에서 해당 엔티티의 기본 키 값을 알아서 사용한다. 

`JPQL`

```sql
select count(m) from Member m // 엔티티 직접 사용 
select count(m.id) from Member m // 엔티티 기본 키 사용 
```

첫 번째 쿼리와 두 번째 쿼리는 동일하게 실행된다. 

## 엔티티를 파라미터로 전달

**엔티티 사용**

```sql
String jpql = "select m from Member m
where m=:member";
List resultList = em.createQuery(jpql)
									.setParameter("member", member1).setResultList();
```

**기본 키 사용**

```sql
String jpql = "select m from Member m
where m.id=:memberId";
List resultList = em.createQuery(jpql)
									.setParameter("memberId", member1Id).setResultList();
```

두 쿼리는 동일하게 실행된다. 

❗외래 키도 동일한 원리로 작동한다. 

→ 연관관계 시 외래 키 사용 = 연관관계 엔티티 직접 사용
