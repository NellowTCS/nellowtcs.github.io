<script>
	import GitHubIcon from '#lib/icons/socials/github.svelte';
	import EmailIcon from '#lib/icons/socials/email.svelte';
	import MastodonIcon from '#lib/icons/socials/mastodon.svelte';
</script>

<div class="socials">
	<a
		href="https://mastodon.social/@nellowtcs"
		target="_blank"
		rel="me noreferrer"
		title="Say Hi on Mastodon"
		aria-label="Say Hi on Mastodon"
	>
		<MastodonIcon />
	</a>
	<a
		href="https://github.com/NellowTCS/"
		target="_blank"
		rel="noopener noreferrer"
		title="See my GitHub profile"
		aria-label="See my GitHub profile"
	>
		<GitHubIcon />
	</a>
	<a
		href="mailto:nellowtcs@gmail.com"
		target="_blank"
		rel="noopener noreferrer"
		title="Send an email"
		aria-label="Send an email"
	>
		<EmailIcon />
	</a>
</div>

<style lang="scss">
	@use '../../scss/breakpoints' as *;
	.socials {
		display: flex;
		align-items: center;
		gap: 4px;

		a {
			transition: all 0.2s ease-in-out;
			display: inline-flex;
			align-items: center;
			justify-content: center;
			flex: 0 0 44px;
			width: 44px;
			height: 44px;
			color: var(--color--text);
			fill: var(--color--text);

			&:hover {
				color: var(--color--primary);
				fill: var(--color--primary);
				filter: drop-shadow(0px 0px 3px var(--color--primary));
			}
		}
	}
</style>
