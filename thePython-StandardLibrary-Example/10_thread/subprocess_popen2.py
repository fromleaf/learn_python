import subprocess

print 'popen2:'
proc = subprocess.Popen(['cat', '-'],
		stdin=subprocess.PIPE,
		stdout=subprocess.PIPE,
		)

msg = 'through stdin to stdout'
stdout_value = proc.communicate(msg)[0]
print '\tpass through: ', repr(stdout_value)
