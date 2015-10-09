package practice01;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Iterator;
import java.util.List;
import java.util.Stack;

import org.omg.CORBA.PUBLIC_MEMBER;

public class Solution {
	public void moveZeroes(int[] nums) {
        int i = 0;
        int j = 0;
        int tmp;
        while (i < nums.length) {
        	if (nums[i] == 0) {
        		j = i;
        		while (j < nums.length - 1) {
					if (nums[j] != 0) {
						break;
					}
					j++;
				}
        		tmp = nums[i];
        		nums[i] = nums[j];
        		nums[j] = tmp;
        	}
        	i++;
        }
    }
	
	public void wiggleSort(int[] nums) {
        int n = nums.length;
        if (n <= 1) return;
        boolean inc = true;
        int prev = nums[0];
        for (int i = 1; i < n; i++) {
        	if ((inc && prev <= nums[i]) || (!inc && prev >= nums[i])) {
        		nums[i - 1] = prev;
        		prev = nums[i];
        	} else {
        		nums[i - 1] = nums[i];
        	}
        	inc = !inc;
        }
    }
	
	public int hIndex(int[] citations) {
        Arrays.sort(citations);
        int h = 0;
        int n = citations.length;
        for (int i = n - 1; i >= 0; i--) {
        	if (citations[i] >= n + 1 - i) h = i;
        }
        return h;
    }
	
	public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        for (int i = 0; i < s.length(); i++) {
			if (s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i) == '[') {
				stack.add(s.charAt(i));
			} else if (s.charAt(i) == ')' && !stack.empty() && stack.peek() == '(') {
				stack.pop();
			} else if (s.charAt(i) == ']' && !stack.empty() && stack.peek() == '[') {
				stack.pop();
			} else if (s.charAt(i) == '}' && !stack.empty() && stack.peek() == '{') {
				stack.pop();
			} else {
				return false;
			}
		}
        if (!stack.empty()) return false;
        return true;
    }
	
	public List<int[]> getSkyline(int[][] buildings) {
		List<int[]> list = new ArrayList<>();
		
		if (buildings.length == 0) return list;
		int row = buildings.length;
		Trples[] trples = new Trples[row];
        for (int i = 0; i < row; i++) {
        	trples[i] = new Trples();
        	trples[i].nums[0] = buildings[i][0];
        	trples[i].nums[1] = buildings[i][1];
        	trples[i].nums[2] = buildings[i][2];
        }
        Comparator<Trples> comparator = new Comparator<Trples>() {

			@Override
			public int compare(Trples o1, Trples o2) {
				// TODO Auto-generated method stub
				if (o1.nums[0] != o2.nums[0]) {
					return o1.nums[0] - o2.nums[0];
				} else if (o1.nums[1] != o2.nums[1]) {
					return o1.nums[1] - o2.nums[1];
				} else {
					return o1.nums[2] - o2.nums[2];
				}
			}
        	
		};
        Arrays.sort(trples, comparator);
        int []tmp;
        for (int i = 0; i < row - 1; i++) {
        	if (trples[i].nums[0] == trples[i + 1].nums[0] && trples[i].nums[0] >= trples[i + 1].nums[0])
        	
        	if (trples[i + 1].nums[0] <= trples[i].nums[1]) {
        		if (trples[i + 1].nums[2] > trples[i].nums[2]) {
        			tmp = new int[2];
        			tmp[0] = trples[i + 1].nums[0];
        			tmp[1] = trples[i + 1].nums[2];
        		} else if (trples[i + 1].nums[2] < trples[i].nums[2]) {
        			tmp = new int[2];
        			tmp[0] = trples[i].nums[1];
        			tmp[1] = trples[i + 1].nums[2];
        		} else {
        			continue;
        		}
        		list.add(tmp);
        	} else {
        		tmp = new int[2];
        		tmp[0] = trples[i].nums[1];
        		tmp[1] = 0;
        		list.add(tmp);
        		tmp = new int[2];
        		tmp[0] = trples[i + 1].nums[0];
        		tmp[1] = trples[i + 1].nums[2];
        		list.add(tmp);
        	}
        }
        tmp = new int[2];
        tmp[0] = trples[row - 1].nums[1];
        tmp[1] = 0;
        list.add(tmp);
        return list;
    }
	
	public class TreeNode {
	      int val;
          TreeNode left;
          TreeNode right;
		  TreeNode(int x) { val = x; }
	}
	
	 public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
	        if (p.right != null) {
	        	TreeNode node = p.right;
	        	while (node.left != null) {
					node = node.left;
				}
	        	return node;
	        }
	        TreeNode succNode = null;
	        while (root != null) {
	        	if (root.val > p.val) {
	        		succNode = root;
	        		root = root.left;
	        	} else if (root.val < p.val) {
	        		root = root.right;
	        	} else {
	        		break;
	        	}
	        }
	        return succNode;
	 }
	 
	 public int numSquares(int n) {
		 int []dp = new int[n+1];
		 Arrays.fill(dp, Integer.MAX_VALUE);
		 
		 for (int i = 0; i*i <= n; i++) dp[i*i] = 1;
		 for (int i = 0; i <= n; i++) {
			 for (int j = 0; i+j*j<=n; j++) {
				 dp[i+j*j] = Math.min(dp[i+j*j], dp[i]+1);
			 }
		 }
		 return dp[n];
	 }
}
