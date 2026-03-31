<script lang="ts">
	import Button from '$lib/components/atoms/Button.svelte';
</script>

<section class="subscribe-section">
	<div class="subscribe-card">
		<div class="content">
			<h2>Subscribe to the newsletter</h2>
			<p>Get notified when I publish new posts. No spam, unsubscribe anytime.</p>
		</div>
		<form action="https://buttondown.com/api/emails/embed-subscribe/NellowTCS" method="post">
			<input type="email" name="email" id="bd-email" placeholder="your@email.com" required />
			<Button type="submit">Subscribe</Button>
		</form>
	</div>
</section>

<style lang="scss">
	@import '$lib/scss/breakpoints.scss';

	.subscribe-section {
		width: 100%;
		max-width: 900px;
		margin: 0 auto;
		padding: 40px 15px;

		@include for-tablet-portrait-up {
			padding: 60px 20px;
		}

		@include for-tablet-landscape-up {
			padding: 80px 30px;
		}
	}

	.subscribe-card {
		background: var(--color--card-background);
		border-radius: 10px;
		box-shadow: var(--card-shadow);
		padding: 30px 20px;
		display: flex;
		flex-direction: column;
		gap: 20px;

		@include for-tablet-portrait-up {
			padding: 40px;
			flex-direction: row;
			align-items: center;
			justify-content: space-between;
		}
	}

	.content {
		display: flex;
		flex-direction: column;
		gap: 8px;

		h2 {
			margin: 0;
			font-family: var(--font--title);
			font-size: 1.4rem;
			font-weight: 700;
		}

		p {
			margin: 0;
			font-size: 0.95rem;
			color: rgba(var(--color--text-rgb), 0.8);
		}
	}

	form {
		display: flex;
		flex-direction: column;
		gap: 12px;
		flex-shrink: 0;

		@include for-tablet-portrait-up {
			flex-direction: row;
			gap: 10px;
		}

		input[type='email'] {
			flex: 1;
			min-width: 200px;
			padding: 10px 16px;
			border: 2px solid rgba(var(--color--text-rgb), 0.2);
			border-radius: 20px;
			font-size: 1rem;
			background: var(--color--page-background);
			color: var(--color--text);
			transition: border-color 0.2s ease;

			&::placeholder {
				color: rgba(var(--color--text-rgb), 0.5);
			}

			&:focus {
				outline: none;
				border-color: var(--color--primary);
			}
		}
	}
</style>
