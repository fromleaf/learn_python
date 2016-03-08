import multiprocessing
import time

def slow_worker():
	print 'Starting worker'
	time.sleep(0.1)
	print 'Finished worker'

if __name__ == '__main__':
	p = multiprocessing.Process(target=slow_worker)
	print 'Before:', p, p.is_alive()

	p.start()
	print 'During:', p, p.is_alive()
	
	p.terminate()
	print 'Terminate:', p, p.is_alive()

	p.join()
	print 'Join:', p, p.is_alive()
