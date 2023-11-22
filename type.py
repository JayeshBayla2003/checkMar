import pyautogui 
import time 

time.sleep(5) 
pyautogui.typewrite(''' 
#include <iostream>
#include <vector>

using namespace std;

int main() {
int n, m;
cin >> n >> m;

vector<vector<char>> city(n, vector<char>(m));
// Read the city map
for (int i = 0; i < n; ++i) {
for (int j = 0; j < m; ++j) {
cin >> city[i][j];
}
}

// Calculate the maximum area of the rectangular building
int maxArea = 0;
vector<int> height(m, 0);
for (int i = 0; i < n; ++i) {
for (int j = 0; j < m; ++j) {
if (city[i][j] == '.') {
height[j]++;
} else {
height[j] = 0;
}
}
// Calculate the maximum area using histogram approach
for (int j = 0; j < m; ++j) {
int minHeight = height[j];
for (int k = j; k < m; ++k) {
if (height[k] == 0) break;
minHeight = min(minHeight, height[k]);
int area = minHeight * (k - j + 1);
maxArea = max(maxArea, area);
}
}
}

cout << maxArea << endl;

return 0;
}

''')