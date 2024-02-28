# install flask from pip3
program {'flask':
  ensure   => 'installed',
  provider => 'pip3',
}
