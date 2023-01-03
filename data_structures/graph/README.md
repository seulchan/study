# Graph

### 공간 복잡도
- Adj. Matrix: O ( V * V )
- Adj. List: O ( V + E )

### 시간 복잡도: 
- 간선 한 개 찾기
  - Adj. Matrix: O ( 1 )
  - Adj. List: O ( V )
- 모든 간선 찾기
  - Adj. Matrix: O ( V * V)
  - Adj. List: O ( V + E )

--- 
그래프가 sparse할 때는 adj. matrix가 adj. list보다 메모리를 더 많이 써야 한다. 간선이 없어서
adj. matrix의 대부분의 요소가 0인데도 불구하고 해당 부분을 포함해 2차원 배열을 만들어야 되기 때문이다. 

그래프가 dense할 때는 adj. matrix가 adj. list보다 더 좋다. 어차피 다 연결되어 있기 때문에 
메모리적 효율성은 동일해지고 정점 i 에서 정점 j 까지의 간선이 있는 확인하는 속도가 더 빠르기 때문에
adj. matrix가 더 빠르다.

## Implementation
- [Graph](implementation/graph.py)
