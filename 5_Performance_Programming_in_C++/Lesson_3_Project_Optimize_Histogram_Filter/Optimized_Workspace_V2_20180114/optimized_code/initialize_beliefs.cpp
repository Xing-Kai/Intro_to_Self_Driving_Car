#include "headers/initialize_beliefs.h"

using namespace std;

// OPTIMIZATION: pass large variables by reference
vector< vector <float> > initialize_beliefs(vector< vector <char> > &grid) {

	// OPTIMIZATION: Which of these variables are necessary?
	// OPTIMIZATION: Reserve space in memory for vectors
  	vector< vector <float> > newGrid;
  	int height = grid.size();
  	int width = grid[0].size();
  	newGrid.reserve(height);
    vector<float> newRow;
	
	float prob_per_cell = 1.0 / ( (float) height * width) ;
  newRow.assign(width, prob_per_cell);
  	// OPTIMIZATION: Is there a way to get the same results 	
  	// without nested for loops?
  	for (int i=0; i<height; i++) {
      newGrid.push_back(newRow);
	}
	return newGrid;
}