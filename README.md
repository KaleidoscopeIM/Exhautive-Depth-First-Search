
# DFS by Gautam Saini and Shilpi FNU #

## Optimized path finding between two locations/cities from a given graph using depth first method.

Run script using &quot;python main.py&quot; then

1. Enter initial location: (eg A1)
2. Enter final location: (eg G1)

Observe the outcomes. First path is traced in alphanumeric order and other 4 path are chosen from 2n possible path combinations where n is number of nodes of the given graph.

List of cities:

[&#39;A5&#39;, &#39;A4&#39;, &#39;A2&#39;, &#39;A1&#39;, &#39;B1&#39;, &#39;B2&#39;, &#39;B3&#39;, &#39;B4&#39;, &#39;B5&#39;, &#39;C2&#39;, &#39;C3&#39;, &#39;C4&#39;, &#39;C5&#39;, &#39;D1&#39;, &#39;D2&#39;, &#39;D3&#39;, &#39;D4&#39;, &#39;D5&#39;, &#39;E4&#39;, &#39;E5&#39;, &#39;F1&#39;, &#39;F2&#39;, &#39;F5&#39;, &#39;G1&#39;, &#39;G2&#39;, &#39;G2b&#39;, &#39;G4&#39;, &#39;G4b&#39;, &#39;G5&#39;]

Enter Initial location: A1

Enter Final location: G1

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

DFS path tracing alphanumeric order: [&#39;A1&#39;, &#39;A2&#39;, &#39;A4&#39;, &#39;A5&#39;, &#39;C5&#39;, &#39;B5&#39;, &#39;B4&#39;, &#39;C4&#39;, &#39;C3&#39;, &#39;B2&#39;, &#39;B1&#39;, &#39;D1&#39;, &#39;D2&#39;, &#39;F2&#39;, &#39;E4&#39;, &#39;D4&#39;, &#39;D5&#39;, &#39;F5&#39;, &#39;E5&#39;, &#39;G4b&#39;, &#39;G2b&#39;, &#39;G2&#39;, &#39;G1&#39;]

A1 to A2 length: 130.0

A2 to A4 length: 305.0

A4 to A5 length: 90.0

A5 to C5 length: 306.0

C5 to B5 length: 229.16587878652442

B5 to B4 length: 36.05551275463989

B4 to C4 length: 96.0

C4 to C3 length: 155.72411502397438

C3 to B2 length: 131.21737689803132

B2 to B1 length: 113.0

B1 to D1 length: 231.0

D1 to D2 length: 126.0

D2 to F2 length: 162.00308639035245

F2 to E4 length: 303.03300150313663

E4 to D4 length: 137.01459776242822

D4 to D5 length: 100.0

D5 to F5 length: 263.0

F5 to E5 length: 81.78630692236935

E5 to G4b length: 140.41723540933285

G4b to G2b length: 231.0

G2b to G2 length: 27.018512172212592

G2 to G1 length: 102.0

Total alphanumeric DFS path length: 3496.4356236230024

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Tracing alternative 4 DFS path in total available combination: 536870912**

Alternative Path 1: [&#39;A1&#39;, &#39;B1&#39;, &#39;B2&#39;, &#39;C2&#39;, &#39;C3&#39;, &#39;C4&#39;, &#39;B4&#39;, &#39;B5&#39;, &#39;A4&#39;, &#39;A5&#39;, &#39;C5&#39;, &#39;D5&#39;, &#39;D4&#39;, &#39;E4&#39;, &#39;E5&#39;, &#39;F5&#39;, &#39;G5&#39;, &#39;G4&#39;, &#39;G2&#39;, &#39;G1&#39;]

A1 to B1 length: 177.0

B1 to B2 length: 113.0

B2 to C2 length: 51.0098029794274

C2 to C3 length: 127.27922061357856

C3 to C4 length: 155.72411502397438

C4 to B4 length: 96.0

B4 to B5 length: 36.05551275463989

B5 to A4 length: 97.082439194738

A4 to A5 length: 90.0

A5 to C5 length: 306.0

C5 to D5 length: 102.0

D5 to D4 length: 100.0

D4 to E4 length: 137.01459776242822

E4 to E5 length: 110.47624178980746

E5 to F5 length: 81.78630692236935

F5 to G5 length: 96.0

G5 to G4 length: 191.0

G4 to G2 length: 232.0

G2 to G1 length: 102.0

Path length: 2401.428237040963

\_\_\_\_\_

Alternative Path 2: [&#39;A1&#39;, &#39;A2&#39;, &#39;B2&#39;, &#39;B1&#39;, &#39;D1&#39;, &#39;D2&#39;, &#39;C2&#39;, &#39;C3&#39;, &#39;C4&#39;, &#39;B4&#39;, &#39;B5&#39;, &#39;C5&#39;, &#39;D5&#39;, &#39;D4&#39;, &#39;E4&#39;, &#39;E5&#39;, &#39;F5&#39;, &#39;G5&#39;, &#39;G4&#39;, &#39;G2&#39;, &#39;G1&#39;]

A1 to A2 length: 130.0

A2 to B2 length: 177.81451009408653

B2 to B1 length: 113.0

B1 to D1 length: 231.0

D1 to D2 length: 126.0

D2 to C2 length: 180.3995565404749

C2 to C3 length: 127.27922061357856

C3 to C4 length: 155.72411502397438

C4 to B4 length: 96.0

B4 to B5 length: 36.05551275463989

B5 to C5 length: 229.16587878652442

C5 to D5 length: 102.0

D5 to D4 length: 100.0

D4 to E4 length: 137.01459776242822

E4 to E5 length: 110.47624178980746

E5 to F5 length: 81.78630692236935

F5 to G5 length: 96.0

G5 to G4 length: 191.0

G4 to G2 length: 232.0

G2 to G1 length: 102.0

Path length: 2754.7159402878838

\_\_\_\_\_

Alternative Path 3: [&#39;A1&#39;, &#39;B1&#39;, &#39;B2&#39;, &#39;C2&#39;, &#39;C3&#39;, &#39;C4&#39;, &#39;B4&#39;, &#39;B5&#39;, &#39;C5&#39;, &#39;D5&#39;, &#39;D4&#39;, &#39;E4&#39;, &#39;E5&#39;, &#39;F5&#39;, &#39;G5&#39;, &#39;G4&#39;, &#39;G2&#39;, &#39;G1&#39;]

A1 to B1 length: 177.0

B1 to B2 length: 113.0

B2 to C2 length: 51.0098029794274

C2 to C3 length: 127.27922061357856

C3 to C4 length: 155.72411502397438

C4 to B4 length: 96.0

B4 to B5 length: 36.05551275463989

B5 to C5 length: 229.16587878652442

C5 to D5 length: 102.0

D5 to D4 length: 100.0

D4 to E4 length: 137.01459776242822

E4 to E5 length: 110.47624178980746

E5 to F5 length: 81.78630692236935

F5 to G5 length: 96.0

G5 to G4 length: 191.0

G4 to G2 length: 232.0

G2 to G1 length: 102.0

Path length: 2137.5116766327496

\_\_\_\_\_

Alternative Path 4: [&#39;A1&#39;, &#39;A2&#39;, &#39;A4&#39;, &#39;B5&#39;, &#39;B4&#39;, &#39;C4&#39;, &#39;C3&#39;, &#39;B2&#39;, &#39;B1&#39;, &#39;D1&#39;, &#39;D2&#39;, &#39;F2&#39;, &#39;E4&#39;, &#39;D4&#39;, &#39;D5&#39;, &#39;F5&#39;, &#39;E5&#39;, &#39;G4b&#39;, &#39;G2b&#39;, &#39;G2&#39;, &#39;G1&#39;]

A1 to A2 length: 130.0

A2 to A4 length: 305.0

A4 to B5 length: 97.082439194738

B5 to B4 length: 36.05551275463989

B4 to C4 length: 96.0

C4 to C3 length: 155.72411502397438

C3 to B2 length: 131.21737689803132

B2 to B1 length: 113.0

B1 to D1 length: 231.0

D1 to D2 length: 126.0

D2 to F2 length: 162.00308639035245

F2 to E4 length: 303.03300150313663

E4 to D4 length: 137.01459776242822

D4 to D5 length: 100.0

D5 to F5 length: 263.0

F5 to E5 length: 81.78630692236935

E5 to G4b length: 140.41723540933285

G4b to G2b length: 231.0

G2b to G2 length: 27.018512172212592

G2 to G1 length: 102.0

Path length: 2968.3521840312155

\_\_\_\_\_
