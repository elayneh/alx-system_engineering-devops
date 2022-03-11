# This puppet manifest is to create a manifest that kills a process killmenow

exec { 'process kill killmenow':
  path    =>'/usr/bin',
  command =>'pkill -f killmenow'
}
