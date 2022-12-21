# acount_book
가계부 프로젝트

## 과제를 하면서 느낀점
1. Django로 할수있는것이 많다는것을 깨달았다.
2. flask api로만 만들어봤던 나는 rest api와 flask api가 매우 비슷하다는것을 알게됬다.
3. 내가 사용 안해본 Django, rest api지만 이 과제를 하면서 많은것을 배우고 느꼈다.

## 기록 목록
1. Django로 database 구축
2. database에 superuser 생성
3. 로그인 웹 페이지를 html로 간단하게 구축
4. Django로 만든 database 서버를 3번에 구축 홈페이지랑 연결
5. 로그인 및 로그아웃 , 회원가입 기능 연결



## 기능요구사항
1. [ ] 고객은 이메일과 비밀번호 입력을 통해서 회원 가입을 할 수 있습니다. 
2. [ ] 고객은 회원 가입이후, 로그인과 로그아웃을 할 수 있습니다. 
3. [ ] 고객은 로그인 이후 가계부 관련 아래의 행동을 할 수 있습니다. 
    1. [ ] 가계부에 오늘 사용한 돈의 금액과 관련된 메모를 남길 수 있습니다. 
    2. [ ] 가계부에서 수정을 원하는 내역은 금액과 메모를 수정 할 수 있습니다. 
    3. [ ] 가계부에서 삭제를 원하는 내역은 삭제 할 수 있습니다. 
    4. [ ] 가계부에서 이제까지 기록한 가계부 리스트를 볼 수 있습니다. 
    5. [ ] 가계부에서 상세한 세부 내역을 볼 수 있습니다. 
    6. [ ] 가계부의 세부 내역을 복제할 수 있습니다.
    7. [ ] 가계부의 특정 세부 내역을 공유할 수 있게 단축 URL을 만들 수 있습니다.
    (단축 URL은 특정 시간 뒤에 만료되어야 합니다.)
4. [ ] 로그인하지 않은 고객은 가계부 내역에 대한 접근 제한 처리가 되어야 합니다.