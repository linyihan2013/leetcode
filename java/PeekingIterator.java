package practice01;

import java.util.Iterator;
import java.util.ListIterator;

public class PeekingIterator implements Iterator<Integer> {

	private boolean flag;
	private Integer integer;
	private Iterator<Integer> iterator;
	public PeekingIterator(Iterator<Integer> iterator) {
	    // initialize any member here.
	    this.iterator = iterator; 
	    flag = false;
	}

    // Returns the next element in the iteration without advancing the iterator.
	public Integer peek() {
        if (!flag) {
        	flag = true;
        	integer = iterator.next();
        }
        return integer;
	}

	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	@Override
	public Integer next() {
	    if (!flag) return iterator.next();
	    flag = false;
	    return integer;
	}

	@Override
	public boolean hasNext() {
	    if (!flag) return iterator.hasNext();
	    return true;
	}

}
