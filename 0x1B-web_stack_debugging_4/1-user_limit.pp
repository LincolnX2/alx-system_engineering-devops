# puppet code to configure possible login with user holberton
# user holberton should be able to open a file without error message
exec { 'debugging soft limit':
  command => "sed -i 's|holberton soft nofile 4|holberton soft nofile 30000|' /etc/security/limits.conf",
  path    => '/bin'
}
exec { 'debugging hard limit':
  command => "sed -i 's|holberton hard nofile 5|holberton hard nofile 50000|' /etc/security/limits.conf",
  path    => '/bin'
}
