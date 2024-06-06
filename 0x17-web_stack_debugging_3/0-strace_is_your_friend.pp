# fix 500 internal error
exec { 'fix-wordpress':
  command     => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path        => ['/bin', '/usr/bin'],
  logoutput   => true,
}
