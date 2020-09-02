#! /bin/bash

# abort on any non-zero return value
set -e
set -o pipefail

TIME=$(date +%Y-%m-%d-%H%M%S)
echo Creating backup $TIME

HIVEMQ_PATH={{ backup_data_path }}
BACKUP_PATH={{ backup_destination_path }}

# backup retained_messages
RETAINED_MESSAGES_PATH=data/persistence/retained_messages
RETAINED_MESSAGES_SOURCE_PATH=$HIVEMQ_PATH/$RETAINED_MESSAGES_PATH/.
RETAINED_MESSAGES_DEST_PATH=$BACKUP_PATH/$TIME/$RETAINED_MESSAGES_PATH/

mkdir -p $RETAINED_MESSAGES_DEST_PATH
cp -r $RETAINED_MESSAGES_SOURCE_PATH $RETAINED_MESSAGES_DEST_PATH

# backup publish_payloads
PUBLISH_PAYLOADS_PATH=data/persistence/publish_payloads
PUBLISH_PAYLOADS_SOURCE_PATH=$HIVEMQ_PATH/$PUBLISH_PAYLOADS_PATH/.
PUBLISH_PAYLOADS_DEST_PATH=$BACKUP_PATH/$TIME/$PUBLISH_PAYLOADS_PATH/

mkdir -p $PUBLISH_PAYLOADS_DEST_PATH
cp -r $PUBLISH_PAYLOADS_SOURCE_PATH $PUBLISH_PAYLOADS_DEST_PATH

# only keep the last seven backups and delete the rest
(cd $BACKUP_PATH && exec rm -rf $(ls -1t | tail -n +8))
