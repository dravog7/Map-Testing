<script lang="ts">
	import type { LatLngTuple, LeafletMouseEvent } from "leaflet";
    import { Marker } from "sveaflet";
	import { createEventDispatcher } from "svelte";
    export let position: number[];

    const dispatch = createEventDispatcher();
    let marker: Marker;

    $: if (marker) {
		marker.on('click', (e: CustomEvent) => {dispatch("click",e);});
	}
</script>

<Marker latLng={[position[0],position[1]]} bind:instance={marker}>
</Marker>