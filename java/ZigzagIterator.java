package practice01;

import java.util.ArrayList;
import java.util.List;

public class ZigzagIterator {
	public List<Integer> v3;
	public int index2 = 0;
    public ZigzagIterator(List<Integer> v1, List<Integer> v2) {
    	v3 = new ArrayList<Integer>();
        int index = 0;
        int times = v1.size() + v2.size();
        int doubles = v1.size() < v2.size() ? v1.size() : v2.size();
        boolean flag = v1.size() < v2.size() ? true : false;
        while (index < times) {
        	if (index < 2*doubles) {
        		if (index % 2 == 0) v3.add(v1.get(index/2));
        		else v3.add(v2.get(index/2));
        	} else {
        		if (flag) v3.add(v2.get(index - doubles));
        		else v3.add(v1.get(index - doubles));
        	}
        	index++;
        }
        index2 = 0;
    }

    public int next() {
    	index2++;
        return v3.get(index2 - 1);
    }

    public boolean hasNext() {
        return index2 < v3.size();
    }
}
