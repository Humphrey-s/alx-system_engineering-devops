# fix 500 internal error
file {'/var/www/html/hum.php':
  ensure  => 'present',
  content => '500 error fixed',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
