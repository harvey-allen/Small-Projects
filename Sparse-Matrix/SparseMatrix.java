import java.util.*;
import java.io.*;

// A class that represents a dense vector and allows you to read/write its elements
class DenseVector {
	private int[] elements;

	public DenseVector(int n) {
		elements = new int[n];
	}

	public DenseVector(String filename) {
		File file = new File(filename);
		ArrayList<Integer> values = new ArrayList<Integer>();

		try {
			Scanner sc = new Scanner(file);

			while (sc.hasNextInt()) {
				values.add(sc.nextInt());
			}

			sc.close();

			elements = new int[values.size()];
			for (int i = 0; i < values.size(); ++i) {
				elements[i] = values.get(i);
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	// Read an element of the vector
	public int getElement(int idx) {
		return elements[idx];
	}

	// Modify an element of the vector
	public void setElement(int idx, int value) {
		elements[idx] = value;
	}

	// Return the number of elements
	public int size() {
		return (elements == null) ? 0 : (elements.length);
	}

	// Print all the elements
	public void print() {
		if (elements == null) {
			return;
		}

		for (int i = 0; i < elements.length; ++i) {
			System.out.println(elements[i]);
		}
	}
}

// A class that represents a sparse matrix
public class SparseMatrix {
	// Auxiliary function that prints out the command syntax
	public static void printCommandError() {
		System.err.println("ERROR: use one of the following commands");
		System.err.println(" - Read a matrix and print information: java SparseMatrix -i <MatrixFile>");
		System.err.println(" - Read a matrix and print elements: java SparseMatrix -r <MatrixFile>");
		System.err.println(" - Transpose a matrix: java SparseMatrix -t <MatrixFile>");
		System.err.println(" - Add two matrices: java SparseMatrix -a <MatrixFile1> <MatrixFile2>");
		System.err.println(" - Matrix-vector multiplication: java SparseMatrix -v <MatrixFile> <VectorFile>");
	}

	public static void main(String[] args) throws Exception {
		if (args.length < 2) {
			printCommandError();
			System.exit(-1);
		}

		if (args[0].equals("-i")) {
			if (args.length != 2) {
				printCommandError();
				System.exit(-1);
			}

			SparseMatrix mat = new SparseMatrix();
			mat.loadEntries(args[1]);
			System.out.println("Read matrix from " + args[1]);
			System.out.println("The matrix has " + mat.getNumRows() + " rows and " + mat.getNumColumns() + " columns");
			System.out.println("It has " + mat.numNonZeros() + " non-zeros");
		} else if (args[0].equals("-r")) {
			if (args.length != 2) {
				printCommandError();
				System.exit(-1);
			}

			SparseMatrix mat = new SparseMatrix();
			mat.loadEntries(args[1]);
			System.out.println("Read matrix from " + args[1] + ":");
			mat.print();
		} else if (args[0].equals("-t")) {
			if (args.length != 2) {
				printCommandError();
				System.exit(-1);
			}

			SparseMatrix mat = new SparseMatrix();
			mat.loadEntries(args[1]);
			System.out.println("Read matrix from " + args[1]);
			SparseMatrix transpose_mat = mat.transpose();
			System.out.println();
			System.out.println("Matrix elements:");
			mat.print();
			System.out.println();
			System.out.println("Transposed matrix elements:");
			transpose_mat.print();
		} else if (args[0].equals("-a")) {
			if (args.length != 3) {
				printCommandError();
				System.exit(-1);
			}

			SparseMatrix mat1 = new SparseMatrix();
			mat1.loadEntries(args[1]);
			System.out.println("Read matrix 1 from " + args[1]);
			System.out.println("Matrix elements:");
			mat1.print();

			System.out.println();
			SparseMatrix mat2 = new SparseMatrix();
			mat2.loadEntries(args[2]);
			System.out.println("Read matrix 2 from " + args[2]);
			System.out.println("Matrix elements:");
			mat2.print();
			SparseMatrix mat_sum1 = mat1.add(mat2);

			System.out.println();
			mat1.multiplyBy(2);
			SparseMatrix mat_sum2 = mat1.add(mat2);

			mat1.multiplyBy(5);
			SparseMatrix mat_sum3 = mat1.add(mat2);

			System.out.println("Matrix1 + Matrix2 =");
			mat_sum1.print();
			System.out.println();

			System.out.println("Matrix1 * 2 + Matrix2 =");
			mat_sum2.print();
			System.out.println();

			System.out.println("Matrix1 * 10 + Matrix2 =");
			mat_sum3.print();
		} else if (args[0].equals("-v")) {
			if (args.length != 3) {
				printCommandError();
				System.exit(-1);
			}

			SparseMatrix mat = new SparseMatrix();
			mat.loadEntries(args[1]);
			DenseVector vec = new DenseVector(args[2]);
			DenseVector mv = mat.multiply(vec);

			System.out.println("Read matrix from " + args[1] + ":");
			mat.print();
			System.out.println();

			System.out.println("Read vector from " + args[2] + ":");
			vec.print();
			System.out.println();

			System.out.println("Matrix-vector multiplication:");
			mv.print();
		}
	}

	// Loading matrix entries from a text file
	// You need to complete this implementation
	public void loadEntries(String filename) {
		File file = new File(filename);

		try {
			Scanner sc = new Scanner(file);
			numRows = sc.nextInt();
			numCols = sc.nextInt();
			entries = new ArrayList<Entry>();
			ArrayList<Integer> values = new ArrayList<Integer>();
			ArrayList<Integer> positions = new ArrayList<Integer>();

			while (sc.hasNextInt()) {
				// Read the row index, column index, and value of an element
				int row = sc.nextInt();
				int col = sc.nextInt();
				int val = sc.nextInt();
				values.add(val);
				// Add your code here to add the element into data member entries
				int pos = (row * numCols) + col; //Calculates the row-major position
				positions.add(pos);
				entries.add(new Entry (pos, val)); //Data memeber entries into dynamic array
			}
			// Add your code here for sorting non-zero elements
			split(0, entries.size() - 1); //Triggers Merge Sort
			for (int i = 0; i < entries.size(); i++) {
				for (int j = 0; j < positions.size(); j ++) {
					if (entries.get(i).getPosition() == positions.get(j)) {
						entries.get(i).setValue(values.get(j)); //Assignment of corrasponding values
					}
				}
			}

		} catch (Exception e) {
			e.printStackTrace();
			numRows = 0;
			numCols = 0;
			entries = null;
		}
	}

	//Recursive function to divide the array in half
	public void split(int startIX, int endIX){
        if(startIX < endIX && (endIX - startIX) >= 1){
            int midPoint = (endIX + startIX) / 2;
            split(startIX, midPoint);
            split(midPoint + 1, endIX);
            merge(startIX, midPoint, endIX); //Merge halves back together
        }
    }

		//Merge sepertaed elements into singular sorted array
		public void merge(int startIX,int midPoint,int endIX) {
	         ArrayList<Integer> sortedArray = new ArrayList<Integer>();
	         int leftIX = startIX;
	         int rightIX = midPoint + 1;

					 //Takes linear time to merge two halves
	         while (leftIX <= midPoint && rightIX <= endIX) {
	             if (entries.get(leftIX).getPosition() <= entries.get(rightIX).getPosition()){
	                 sortedArray.add(entries.get(leftIX).getPosition());
	                 leftIX = leftIX + 1;
	             } else {
	                 sortedArray.add(entries.get(rightIX).getPosition());
	                 rightIX = rightIX + 1;
	             }
	         }
	         while (leftIX <= midPoint) {
	             sortedArray.add(entries.get(leftIX).getPosition());
	             leftIX = leftIX + 1;
	         }
	         while (rightIX <= endIX) {
	             sortedArray.add(entries.get(rightIX).getPosition());
	             rightIX = rightIX + 1;
	         }
	         int i = 0;
	         int count = startIX;
	         while (i < sortedArray.size()) {
	             entries.get(count).setPosition(sortedArray.get(i++)); //Assigns new positions
	             count = count + 1;
	         }
	     }

	// Default constructor
	public SparseMatrix() {
		numRows = 0;
		numCols = 0;
		entries = null;
	}

	// A class representing a pair of column index and elements
	private class Entry {
		private int position; // Position within row-major full array representation
		private int value; // Element value

		// Constructor using the column index and the element value
		public Entry(int pos, int val) {
			this.position = pos;
			this.value = val;
		}

		// Copy constructor
		public Entry(Entry entry) {
			this(entry.position, entry.value);
		}

		// Read column index
		int getPosition() {
			return position;
		}

		// Set column index
		void setPosition(int pos) {
			this.position = pos;
		}

		// Read element value
		int getValue() {
			return value;
		}

		// Set element value
		void setValue(int val) {
			this.value = val;
		}
	}

	// Adding two matrices
	public SparseMatrix add(SparseMatrix M) {
		// Add your code here
		SparseMatrix resultMatrix = new SparseMatrix(); //Independant
		resultMatrix.entries = new ArrayList<Entry>();
		ArrayList<Integer> tempMatrix = new ArrayList<Integer>();
		resultMatrix.numRows = numRows;
		resultMatrix.numCols = numCols;
		while(tempMatrix.size() < (numRows * numCols)) tempMatrix.add(0);

		//Algorithm to construct matrix sum (Time Complexity; O(N1 + N2))
		for (int i = 0; i < entries.size(); i++) { //Time Complexity; O(N)
			int pos = entries.get(i).getPosition();
			int val = entries.get(i).getValue();
			tempMatrix.set(pos, val);
		}
		for (int j = 0; j < M.entries.size(); j++) { //Time Complexity; O(N)
			if (tempMatrix.get(M.entries.get(j).getPosition()) != 0) {
				int pos = M.entries.get(j).getPosition();
				int val1 = tempMatrix.get(pos);
				int val2 = M.entries.get(j).getValue();
				int addResult = val1 + val2; //Performs calculation
				tempMatrix.set(pos, addResult);
			} else {
				int pos = M.entries.get(j).getPosition();
				int val = M.entries.get(j).getValue();
				tempMatrix.set(pos, val);
			}
		}
		//End of Algorithm
		for (int i = 0; i < (numRows * numCols); i++) {
			if (tempMatrix.get(i) != 0) { //Does not store 'new' zeros
				resultMatrix.entries.add(new Entry (i, tempMatrix.get(i)));
			}
		}
		return resultMatrix;
	}

	// Transposing a matrix
	public SparseMatrix transpose() {
		// Add your code here
		SparseMatrix transposedMatrix = new SparseMatrix(); //Independant
		transposedMatrix.entries = new ArrayList<Entry>();
		ArrayList<Integer> positions = new ArrayList<Integer>();
		HashMap<Integer, Integer> posVal = new HashMap<Integer, Integer>();
		transposedMatrix.numRows = numCols;
		transposedMatrix.numCols = numRows;
		//Recalculates Position
		for (int i = 0; i < entries.size(); i++) {
			int tempPos = entries.get(i).getPosition();
			double rmRow = Math.floor(tempPos / numCols); //Row Index
			double rmCol = Math.floor(tempPos - (rmRow * numCols)); //Column Index
			tempPos = ((int)rmCol * numRows) + (int)rmRow; //Column Major Position
			positions.add(tempPos);
			int val = entries.get(i).getValue();
			posVal.put(tempPos, val);
		}
		Collections.sort(positions); //Sorts positions to allow for print
		for (int i = 0; i < positions.size(); i++) { //Re-Assigns values to correct position
		  transposedMatrix.entries.add(new Entry (positions.get(i), posVal.get(positions.get(i))));
		}
		return transposedMatrix;
	}

	// Matrix-vector multiplication
	public DenseVector multiply(DenseVector v) {
		// Add your code here
		DenseVector multipliedVector = new DenseVector(numRows); //Independant
		for (int i = 0; i < entries.size(); i++) {
			int val = entries.get(i).getValue();
			int pos = entries.get(i).getPosition();
			double rowPos = Math.floor(pos / numCols); //Row Index
			double colPos = Math.floor(pos - (rowPos * numCols)); //Col Index
			int vectorVal = v.getElement((int)colPos);
			int currentVal =  multipliedVector.getElement((int)rowPos);
			multipliedVector.setElement((int)rowPos, currentVal + (vectorVal * val));
			}
		return multipliedVector;
	}

	// Return the number of non-zeros
	public int numNonZeros() {
		// Add your code here
		int numberNonZero = entries.size();
		return numberNonZero;
	}

	// Multiply the matrix by a scalar, and update the matrix elements
	public void multiplyBy(int scalar) {
		// Add your code here
		for (int i = 0; i < entries.size(); i++)
			entries.get(i).setValue(entries.get(i).getValue() * scalar);
	}

	// Number of rows of the matrix
	public int getNumRows() {
		return this.numRows;
	}

	// Number of columns of the matrix
	public int getNumColumns() {
		return this.numCols;
	}

	// Output the elements of the matrix, including the zeros
	// Do not modify this method
	public void print() {
		int n_elem = numRows * numCols;
		int pos = 0;

		for (int i = 0; i < entries.size(); ++i) {
			int nonzero_pos = entries.get(i).getPosition();

			while (pos <= nonzero_pos) {
				if (pos < nonzero_pos) {
					System.out.print("0 ");
				} else {
					System.out.print(entries.get(i).getValue());
					System.out.print(" ");
				}

				if ((pos + 1) % this.numCols == 0) {
					System.out.println();
				}

				pos++;
			}
		}

		while (pos < n_elem) {
			System.out.print("0 ");
			if ((pos + 1) % this.numCols == 0) {
				System.out.println();
			}

			pos++;
		}
	}

	private int numRows; // Number of rows
	private int numCols; // Number of columns
	private ArrayList<Entry> entries; // Non-zero elements
}
