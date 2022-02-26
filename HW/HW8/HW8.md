### Study Group

Shenghan Zheng 3037534676

### 2 (Max-Flow) a cohort of spies

#### Main Idea

Set all cities as vertices

First, denote each spy's path as a unit flow. We want a set of paths for each spy to go from source s to any vertex in T.

To achieve this, we add a source s and add (s,s_i) to the edge set and set their capacity to be 1. Likewise, we add a sink vertex t and add (p,t) to the edge set for every vertex in T(denoted by p) and assign their value to be positive infinity. Then, we split each vertex into v_in and v_out. v_in has all incoming edges of v while v_out has all outgoing edges of v. Assign the capacity of (v_in,v_out) to be c.

Since the source has k outgoing edges with same capacity of 1. The maximum flow should be less than k. Run Ford-Fulkerson to solve this problem. If the max flow is less than k. It indicates that the requirement can't be met. If the max flow is k, then we find a set of paths for each spy that satisfies the requirement.

### 3 (Max Flow LP) Min Cost Flow 

#### (a)

Construct linear program

![image-20211022181409218](C:\Users\Eric Zheng\AppData\Roaming\Typora\typora-user-images\image-20211022181409218.png)

Since the linear program can be solved in polynomial time, the minimum cost flow problem can be solved in polynomial time

#### (b)

Let‘s say we want to find the shortest path from p to q

Set capacity to each edge to be positive infinity(ignore capacity)

Set each edge's cost to be its distance(or weight)

Add a source s and add (s,p) to E and the capacity and cost of (s,p) is 1. Add a sink t and add (q,t) to E and the capacity and cost of (q,t) is 1

Now run Ford-Folkerson for (s,t), the result is the minimum path from p to q

#### Proof

After modifying, the objective function becomes: sum of weight + 2

If we find a flow with the minimum value, we have the minimum path from p to q. Because the capacity for the source is only 1 and min flow means min distance.

#### (c) 

Set cost for all edges to be 0

Add (t,s) to E with positive infinite capacity and -1 cost

Now run Ford-Folkerson for (s,t)

Proof:

The augmented path will be continuously added to the flow, since going through (t,s) is the only way to reduce the cost from s to t. The algorithm will end when there is no augmented path which is the end of the max-flow problem



### 4 Faster Maximum Flow

#### (a)

#### Main Idea

1. Add a new weight 1 to each edge
2. Run BFS according to the new edge with root s

#### Correctness

BFS will guarantee that the height of t is minimum(blackbox). Thus, it's the shortest distance path by definition

#### Runtime

add new weight O(m)

Run BFS O(m+n)

total runtime O(m+n)

#### (b)

#### Proof

After running each augmentation in the graph. We will remove at least one forward edge from s to t and add a back edge. Since the back edge only go up 1 layer, it will not decrease the distance from s to t. Otherwise, suppose we get a smaller distance by using this back edge(named (p,q)), then q has a smaller distance compared to the vertex used in the minimum path at the same layer.  Contradiction!

#### (c)

#### Proof

Notice that every time we do the flow augmentation, one forward edge will be removed and we will replace it with a reverse edge. 

Lemma: If we add previous deleted edge from after one augmentation and include it in the shortest path, then our distance add 1.

Let's say edge (u,v) is critical if it's the edge to be removed in the residual graph. u, v are in the layer i, i+1 respectively of BFS tree. To make (u, v) add to the augmenting path again, u must appear in a level higher then v since (v, u) should be the saturated edge included in the augmenting path to make it reverse.

Since the distance from s to v never decreases, the level of v will be equal or greater than i+1. Thus, u must rise to level at least i+2. Thus, after adding (u, v) again, our distance add at least 1

Back to the problem, if none of the edges will be added again in the original graph, it indicates that we remove all m edges one time and reverse them. After m-1 iterations, we have 1 outgoing edge from s that isn't reversed. Otherwise we can't reach t.That means the last path is directly from s to t but its distance is 1 which shows that the distance of previous m-1 paths is 1 which is impossible. Thus, we must add a edge that is previously deleted in the graph.  According to the lemma, the statement holds

#### (d)

From c) we know that the distance of u will increase at least 2 since its level changes from i to at least i+2. Notice that the BFS tree has no levels numbered above n. Thus, the total time that one edge occur as a critical edge is at most n/2. There are at most 2m edges(including the reverse edge) will appear during the iterations. Since we handle at least one critical edge for 1 iteration, we will do O(mn) augmentations

### 5 Jumbled Sequences

#### Main Idea

1. store the sequence as vertices with their values

2. Add a source s and connect it with the first 2k vertices. Add a sink t and add (p,t) in E(p are all last 2k vertices). All edges with capacity 1

3. For the n vertices(except s,t), 

   For i in range(n):

     For j in range(2k):

   ​	if |a_i - a_(i+j)|<=2:

   ​		add (a_i, a_(i+j)) to E

4. For the n vertices(except s,t), split each one of them into 2 vertices v_in, v_out such that v_in has all the incoming edges while v_out has all the outgoing edges. Add (v_in, v_out) to E with capacity 1.

5. Run Ford-Fulkerson



#### Runtime

Construct the graph is O(nk)

s has 2k outgoing edges. t has 2k incoming edges. For any of the n vertices, each of them has at most 2k edges. The split of vertices will add n edges. Thus, the total number of edges is at most 4k+2kn+n 

The max flow is less than 2k since s only has 2k outgoing edges with each capacity equals 1.

Total runtime = O(2k(4k+2kn+n)+nk) = O(nk^2)

