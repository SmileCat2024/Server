<?php

// Load Composer autoloader
require __DIR__ . '/../vendor/autoload.php';

// Initialize Flextype
use Flextype\Flextype;

$app = new Flextype(__DIR__ . '/..');

// Run Flextype
$app->run();