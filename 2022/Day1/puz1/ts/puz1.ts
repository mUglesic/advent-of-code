
const data: string[] = Deno.readTextFileSync(`./${Deno.args[0]}`).split('\n');

let part = 0;

const amts: number[] = [];

for (const line of data) {

    if (line === '') {
        amts.push(part);
        part = 0;
        continue;
    }

    part += parseInt(line);

}

console.log(amts.sort((a, b) => b - a).slice(0, 3).reduce((sum, current) => sum + current));