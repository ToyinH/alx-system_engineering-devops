# A puppet manifest that kills a process named killmenow

exec {
  'kill now':
    command  => 'pkill -f killmenow',
    provider => 'shell',
}
