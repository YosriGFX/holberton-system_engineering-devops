# Fixed and automated with Puppet
exec { 'fixing WP setting issues':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}
