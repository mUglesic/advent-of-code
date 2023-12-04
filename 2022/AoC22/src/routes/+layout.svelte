
<svelte:head>
    <link rel="stylesheet" href="/styles/fonts.css">
</svelte:head>

<div class="">

    <h1>Advent of Code 2022</h1>

    <slot></slot>

</div>

<style>

    :global(body, html) {
        margin: 0;
        padding: 0;
    }

    :global(body) {
        background-color: hsl(180, 38%, 13%);
    }

    h1 {
        text-align: center;
        font-family: 'Alpha Prota', monospace;
        font-size: 4rem;
        color: white;
    }

</style>