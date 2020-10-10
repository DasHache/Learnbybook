#include <bits/stdc++.h>
// task for several test cases
// the bounciness is an interval including the max and the min
//the min and the max bounciness are on two diff lines

signed main() {
    cin.tie(0);
    ios_base::sync_with_stdio(false);

    int cases, nodes, start, finish, node;
    cin >> cases;
    

    for (int c = 0; c < cases; c++){
        cin >> nodes >> start >> finish;
            
    
        vector <int> jmin (nodes, 0);
        vector <int> jmax (nodes, 0);

        for (auto i = 0; i < nodes; i++){
            cin >> jmin[i];
        }
        for (int i = 0; i < nodes; i++){
            cin >> jmax[i];
        }

        queue <int> q;

        q.push(start);
        vector <int> dist(nodes, -1);
        dist[start] = 0;
        while(!q.empty()){
            node = q.front(); //top of the queue
            q.pop();
            for (int i = jmin[node]; i < jmax[node] + 1; i++){
                if (node + i > nodes) break;
                if (dist[node + i] == -1){
                    //if (find(begin(q), end(q), node + i) != )
                    q.push(node + i);
                    dist[node + i] = dist[node] + 1;
                }
            }
            if (dist[finish] > -1) break;
            for (int i = jmin[node]; i < jmax[node] + 1; i++){
                if (node - i < 0)break;
                if (dist[node - i] == -1){
                    q.push(node - i);
                    dist[node - i] = dist[node] + 1;
                }
            }
            if (dist[finish] > -1) break;
        }
    
        cout << "Case #" << c << ": " << dist[finish] << endl;
    
    }
}