# Creates a file /tmp/holberton with certain permissions, content, owner/group
file { '/tmp/holberton':
  ensure  => file,
  mode    => '0744',
  owner   => www-data,
  group   => www-data,
  content => 'I love Puppet',
}
