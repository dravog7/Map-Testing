<script lang="ts">
    export let wifiInfo: any;
    export let index: number;

    let filterText: string;

    $: filterSignature = wifiInfo.signature.filter((it: { address: string | any[]; }) => !filterText || it.address.includes(filterText))
</script>

<div class="flex flex-col p-2 h-full">
    <p>Index: {index}</p>
    <p>TimeStamp: {new Date(wifiInfo.timeStamp*1000).toLocaleString()}</p>
    <p>deviceId: {wifiInfo.deviceId}</p>
    <p>Latitude: {wifiInfo.location.latitude}</p>
    <p>longitude: {wifiInfo.location.longitude}</p>
    <p>Device Type: {wifiInfo.deviceType}</p>

    <p>
        Filter signature: 
        <input type="text" bind:value={filterText} placeholder="contains"/>
    </p>

    <table class="table-auto border-collapse border border-slate-500 overflow-x-scroll">
        <tr>
            <th class="px-1 border border-slate-500">address</th>
            <th class="px-1 border border-slate-500">channel</th>
            <th class="px-1 border border-slate-500">frequency</th>
            <th class="px-1 border border-slate-500">signalLevel</th>
        </tr>
        {#each filterSignature as ap}
            <tr>
                <td class="px-1 border border-slate-500">{ap.address}</td>
                <td class="px-1 border border-slate-500">{ap.channel}</td>
                <td class="px-1 border border-slate-500">{ap.frequency}</td>
                <td class="px-1 border border-slate-500">{ap.signalLevel}</td>
            </tr>
        {/each}
    </table>
</div>