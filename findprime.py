# Generate prime numbers
# Found at  http://www.raspberrypi-spy.co.uk/2012/06/overclocking-benchmarking-the-raspberry-pi/
# Based on an article from http://dunningrb.wordpress.com/
 
import utime, sys
 
# Function to print message
def print_prime(x):
  print (" Prime : %7i " %x)
 
# Function to search for prime numbers
# within number range
def find_primes(upper_limit):
  count = 0
  candidate = 3
  while(candidate <= upper_limit):
    trial_divisor = 2
    prime = 1 # assume it's prime
    while(trial_divisor**2 <= candidate and prime):
      if(candidate%trial_divisor == 0):
        prime = 0 # it isn't prime
      trial_divisor+=1
    if(prime):
      #print_prime(candidate)
      count += 1
    candidate += 2
  return count
# Check if the script was called with a
# parameter. Use that as the upper limit
# of numbers to search
if len(sys.argv) != 2:
  upper_limit=50000
else:
  upper_limit=int(sys.argv[1])
 
# Record the current time
startTime = utime.ticks_ms()
# Start the process
print("")
print ("Sieve of Eratosthenes - LoPy")
print ("%d Iterations" %(upper_limit))
print ("")
count = find_primes(upper_limit)
 
# Measure and print the elapsed time
elapsed=utime.ticks_ms()-startTime
print (" Found %d primes in %s ms" %(count,elapsed))
