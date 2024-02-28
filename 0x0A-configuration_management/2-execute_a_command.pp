# kills a process
exec {'kills a process':

  command => 'pkill killmenow',
  path    => '/bin/',
  }
