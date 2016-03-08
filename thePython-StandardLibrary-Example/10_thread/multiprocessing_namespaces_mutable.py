import multiprocessing

def producer(ns, event):
	# never update global variable
	ns.my_list.append('This is the value')
	event.set()

def consumer1(ns, event):
	print 'consumer1 Before event:', ns.my_list
	event.wait()
	print 'consumer1 After event:', ns.my_list

def consumer2(ns, event):
	print 'consumer2 Before event:', ns.my_list
	event.wait()
	print 'consumer2 After event:', ns.my_list

if __name__ == '__main__':
	mgr = multiprocessing.Manager()
	namespace = mgr.Namespace()
	namespace.my_list = []

	event = multiprocessing.Event()
	
	p = multiprocessing.Process(target=producer,
								args=(namespace, event))
	c1 = multiprocessing.Process(target=consumer1,
								args=(namespace, event))
	c2 = multiprocessing.Process(target=consumer1,
								args=(namespace, event))

	c1.start()
	p.start()


	c1.join()
	p.join()
	print 'in main', namespace.my_list
