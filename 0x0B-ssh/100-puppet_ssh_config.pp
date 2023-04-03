# Changes configuration file to turn off password authent. and use private key
file { '/etc/ssh/ssh_config':
  content => 'PasswordAuthentication no
  IdentityFile ~/.ssh/school',
}
