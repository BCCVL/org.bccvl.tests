#!/usr/bin/perl -w
# author: stanley@intersect.org.au
# Used to quickly generate a page of file exists assertions for experiment results pages
# from the copy paste of a experiments result page.

# looks for a file called data.txt with the copy paste of the experiment results page
# the data.txt has been preprocessed (vim find and replace) to remove any blank lines as well as
# the leading 'd' character that seems to be on each line for some reason.

# the script takes into account algorithm sections with the mode variable by looking for lines
# beginning with the testName.

# It also spits out the total number of experiment files assertion at the end

# ********************************************************************************************** #
# This needs to include the entirety of the name up until just before the algorithm to work **** #
# ********************************************************************************************** #
$testName = "gam_circles_ch_bioclim_1km_quad_20140717113934 - ";

open (my $FILE, "<", "data.txt") or die "can't open the file";

my @lines = <$FILE>;

$total = 0;
$mode = "MODE_NOT_FOUND!";
for my $line (@lines) {
    # Look for the algorithm name.
    if ($line =~ /$testName([a-z]+)/) {
        $mode = $1;
        print "\n";
    } else {
        chomp $line;
        print "self.assertTrue(experiment_view.has_result_file('$line', '$mode'))\n";
        $total++;
    }
}

print "\nself.assertEqual($total, experiment_view.get_num_output_files())\n";
