## 영속성 전이란?

특정 엔티티를 영속 상태로 만들 때, 연관된 엔티티도 함께 영속 상태로 만드는 것

### 사용 방법

부모쪽에 옵션을 넣는다. 

```jsx
@OneToMany(mappedBy="parent", cascade=CascadeType.PERSIST)
```

## 고아 객체란?

부모 엔티티와 연관 관계가 끊어진 자식 엔티티를 의미한다.

예를 들어, 자식 엔티티를 부모가 가지고 있는 컬렉션에서 제거했을 때 지워진 자식 엔티티를 고아 객체라 한다. 

```jsx
Parent parent = em.find(Parent.class, id);
parent.getChildren().remove(0);  // 제거

```

## 고아 객체 제거 기능

참조가 제거된 엔티티는 다른 곳에서 참조하지 않는다고 판단하여 삭제하는 기능이다.

### 사용 방법

부모쪽에 옵션을 넣는다. 

```jsx
@OneToMany(mappedBy="parent", cascade=CascadeType.PERSIST, orphanRemoval = true)
```

### 📌 주의

- 참조하는 곳이 하나일 때 사용!
- 특정 엔티티가 개인 소유할 때 사용!
- @OneToXXX만 사용 가능

## 영속성 전이+고아 객체 생명 주기

CascadeType.All + orphanRemoval=true 

⇒ 부모 엔티티를 통해 자식의 생명 주기 관리 가능
