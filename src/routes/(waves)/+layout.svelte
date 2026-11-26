<script>
	import Waves from '#lib/components/organisms/Waves.svelte';
	import Header from '#lib/components/organisms/Header.svelte';
	import Footer from '#lib/components/organisms/Footer.svelte';

	import { absoluteUrl, description, image, keywords, title } from '#lib/data/meta';
</script>

<svelte:head>
	<link rel="canonical" href={absoluteUrl()} />
	<meta name="keywords" content={keywords.join(', ')} />

	<meta name="description" content={description} />
	<meta property="og:description" content={description} />
	<meta name="twitter:description" content={description} />

	<title>{title}</title>
	<meta property="og:title" content={title} />
	<meta name="twitter:title" content={title} />

	<meta property="og:image" content={image} />
	<meta name="twitter:image" content={image} />

	<meta property="og:url" content={absoluteUrl()} />
	<meta property="og:type" content="website" />
	<meta name="twitter:card" content="summary_large_image" />
</svelte:head>

<Waves />

<Header />

<main>
	<slot />
</main>

<Footer />
