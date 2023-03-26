# Executes the pkill command to kill process named killmenow
exec { 'pkill':
  command => '/usr/bin/pkill killmenow',
}
