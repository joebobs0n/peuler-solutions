#!/usr/bin/zsh


format_END="\033[0m"
format_BOLD="\033[1m"
format_INVERT="\033[3m"
format_UNDERLINE="\033[4m"
format_DARKCYAN="\033[36m"
format_GRAY="\033[90m"
format_RED="\033[91m"
format_GREEN="\033[92m"
format_YELLOW="\033[93m"
format_BLUE="\033[94m"
format_PURPLE="\033[95m"
format_CYAN="\033[96m"
function info    { echo "${format_GREEN}-I-${format_END} ${format_GRAY}[ new-solution.zsh ]${format_END} $argv[1]" }
function warning { echo "${format_YELLOW}-W-${format_END} ${format_GRAY}[ new-solution.zsh ]${format_END} $argv[1]" }
function fatal   { echo "${format_RED}-F-${format_END} ${format_GRAY}[ new-solution.zsh ]${format_END} $argv[1]"; exit 1 }


num_args=1
description=""
args="<problem_number>"
usage_str="${format_BOLD}Usage${format_END}: ${format_DARKCYAN}./new-solution.zsh ${args}${format_END}"
if [[ $argv[1] == '-h' || $argv[1] == '--help' ]]; then
    [[ $( echo ${description} ) != "" ]] && echo "${format_BOLD}Description${format_END}: ${description}"
    echo "${usage_str}"
    exit 0
fi
[[ $# < ${num_args} ]] && fatal "Insufficient required args\n${usage_str}"

pnum=${argv[1]}
outname="solutions/$( printf '%03d' ${pnum} ).py"
if [[ -e ${outname} ]]; then
    fatal "solution script for given problem number already exists"
fi
info "creating solution script for problem number ${format_BOLD}${pnum}${format_END}... [${format_DARKCYAN}${outname}${format_END}]"
prompt=$( curl "https://projecteuler.net/problem=${pnum}" 2> /dev/null | grep 'problem_content' -A 100 | grep '</div><br>' -B 100 -m 1 | sed 's|<sup>|^|g' | sed -E 's|</?[^>]+>||g' | tr '\n' ' ' | sed -E 's/(^\s+|\s+$)//g' )
cp "src/template" ${outname}
sed -i "s/\#pnum\#/${pnum}}/g" ${outname}
sed -i "s/\#prompt\#/${prompt}/g" ${outname}
echo "\nPrompt: ${prompt}"
